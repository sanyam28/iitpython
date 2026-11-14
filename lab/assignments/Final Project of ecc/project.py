import matplotlib.pyplot as plt
import numpy as np


class DenseLayer:
    """Fully Connected (Dense) Layer with explicit gradient and parameter tracking."""

    def __init__(self, in_dim: int, out_dim: int):
        # He (Kaiming) Initialization to preserve variance with ReLU activations
        self.W = np.random.randn(in_dim, out_dim) * np.sqrt(2.0 / in_dim)
        self.b = np.zeros((1, out_dim))

        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)
        self.X = None

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass: Z = X * W + b"""
        self.X = X
        return np.dot(X, self.W) + self.b

    def backward(self, dZ: np.ndarray) -> np.ndarray:
        """Backward pass: Computes parameter derivatives via the Chain Rule."""
        self.dW = np.dot(self.X.T, dZ)
        self.db = np.sum(dZ, axis=0, keepdims=True)
        return np.dot(dZ, self.W.T)


class ContinualLearningEngine:
    """Multi-Layer Neural Network Engine implementing Elastic Weight Consolidation (EWC)

    from first principles in pure NumPy.
    """

    def __init__(self, layer_sizes: list):
        self.layers = [
            DenseLayer(layer_sizes[i], layer_sizes[i + 1])
            for i in range(len(layer_sizes) - 1)
        ]
        self.fisher_matrix = {}
        self.optimal_params = {}
        self.activations = []

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward propagation through dense layers and ReLU non-linearities."""
        out = X
        self.activations = [X]
        for i, layer in enumerate(self.layers):
            out = layer.forward(out)
            if i < len(self.layers) - 1:
                out = np.maximum(0, out)  # ReLU non-linearity
            self.activations.append(out)
        return out

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Generates class index predictions from logits."""
        logits = self.forward(X)
        return np.argmax(logits, axis=1)

    def softmax_cross_entropy(
        self, logits: np.ndarray, y: np.ndarray
    ) -> tuple:
        """Numerically stable Softmax output activation combined with

        Categorical Cross-Entropy Loss.
        """
        # Shift logits by max per sample to prevent numerical overflow in e^z
        logits_shifted = logits - np.max(logits, axis=1, keepdims=True)
        exp_s = np.exp(logits_shifted)
        probs = exp_s / np.sum(exp_s, axis=1, keepdims=True)

        N = len(y)
        loss = -np.mean(np.log(probs[range(N), y] + 1e-12))

        # Analytical gradient of combined Softmax + Cross-Entropy w.r.t. Logits (dZ = P - Y) / N
        dZ = probs.copy()
        dZ[range(N), y] -= 1.0
        dZ /= N
        return loss, dZ, probs

    def compute_fisher_information(self, X: np.ndarray, y: np.ndarray):
        """Computes the diagonal elements of the empirical Fisher Information Matrix

        (F_i) for Task A parameters to quantify their importance.
        """
        print(
            '\n[EWC Engine] Estimating Fisher Information Matrix for Task A...'
        )
        for i, layer in enumerate(self.layers):
            self.fisher_matrix[f'W_{i}'] = np.zeros_like(layer.W)
            self.fisher_matrix[f'b_{i}'] = np.zeros_like(layer.b)
            self.optimal_params[f'W_{i}'] = layer.W.copy()
            self.optimal_params[f'b_{i}'] = layer.b.copy()

        num_samples = len(X)
        for idx in range(num_samples):
            x_i = X[idx : idx + 1]
            y_i = y[idx : idx + 1]

            logits = self.forward(x_i)
            _, dZ, _ = self.softmax_cross_entropy(logits, y_i)

            # Sample-level backpropagation to gather squared gradients
            for l in reversed(range(len(self.layers))):
                layer = self.layers[l]
                dW = np.dot(self.activations[l].T, dZ)
                db = np.sum(dZ, axis=0, keepdims=True)

                self.fisher_matrix[f'W_{l}'] += (dW**2) / num_samples
                self.fisher_matrix[f'b_{l}'] += (db**2) / num_samples

                dZ = np.dot(dZ, layer.W.T)
                if l > 0:
                    dZ[self.activations[l] <= 0] = 0

    def train_task(
        self,
        X: np.ndarray,
        y: np.ndarray,
        epochs: int = 50,
        lr: float = 0.05,
        ewc_lambda: float = 0.0,
    ) -> list:
        """Trains the model on a task.

        When ewc_lambda > 0, injects Fisher-weighted quadratic parameter penalties to protect Task A knowledge.
        """
        loss_history = []
        num_samples = len(X)

        for epoch in range(1, epochs + 1):
            logits = self.forward(X)
            base_loss, dZ, _ = self.softmax_cross_entropy(logits, y)

            # Calculate EWC Regularization Loss Penalty
            ewc_penalty = 0.0
            if ewc_lambda > 0 and self.fisher_matrix:
                for i, layer in enumerate(self.layers):
                    ewc_penalty += np.sum(
                        self.fisher_matrix[f'W_{i}']
                        * (layer.W - self.optimal_params[f'W_{i}']) ** 2
                    )
                    ewc_penalty += np.sum(
                        self.fisher_matrix[f'b_{i}']
                        * (layer.b - self.optimal_params[f'b_{i}']) ** 2
                    )
                ewc_penalty *= ewc_lambda / 2.0

            total_loss = base_loss + ewc_penalty
            loss_history.append(total_loss)

            # Backpropagation
            for l in reversed(range(len(self.layers))):
                layer = self.layers[l]
                dX = layer.backward(dZ)

                # Inject EWC Regularization Gradient Component: lambda * F_i * (theta_i - theta_A,i*)
                if ewc_lambda > 0 and self.fisher_matrix:
                    ewc_grad_W = (
                        ewc_lambda
                        * self.fisher_matrix[f'W_{l}']
                        * (layer.W - self.optimal_params[f'W_{l}'])
                    )
                    ewc_grad_b = ewc_lambda * self.fisher_matrix[
                        f'b_{l}'
                    ] * (layer.b - self.optimal_params[f'b_{l}'])

                    # Clip EWC gradient component to ensure numerical stability
                    np.clip(ewc_grad_W, -1.0, 1.0, out=ewc_grad_W)
                    np.clip(ewc_grad_b, -1.0, 1.0, out=ewc_grad_b)

                    layer.dW += ewc_grad_W
                    layer.db += ewc_grad_b

                # Stochastic Gradient Descent parameter update
                layer.W -= lr * layer.dW
                layer.b -= lr * layer.db

                dZ = dX
                if l > 0:
                    dZ[self.activations[l] <= 0] = 0

        return loss_history


# --- EXPERIMENTAL BENCHMARK PIPELINE ---
def run_continual_learning_experiment():
    np.random.seed(42)

    # 1. Generate Non-Linear Synthetic Task Sequences
    # Task A: Classify non-linear feature interaction across features 0 & 1
    X_A = np.random.randn(400, 8)
    y_A = (X_A[:, 0] + X_A[:, 1] > 0).astype(int)

    # Task B: Classify non-linear feature interaction across features 6 & 7
    X_B = np.random.randn(400, 8)
    y_B = (X_B[:, 6] - X_B[:, 7] > 0).astype(int)

    print('==================================================================')
    print('   CONTINUAL LEARNING VIA EWC ENGINE - EXPERIMENTAL BENCHMARK   ')
    print('==================================================================')

    # --- EXPERIMENT 1: Naive Sequential Fine-Tuning (lambda = 0.0) ---
    print('\n[REGIME 1] Running Naive Sequential Fine-Tuning (lambda = 0.0)...')
    naive_model = ContinualLearningEngine(layer_sizes=[8, 32, 16, 2])

    loss_A_naive = naive_model.train_task(X_A, y_A, epochs=50, lr=0.05)
    acc_A_naive_initial = np.mean(naive_model.predict(X_A) == y_A)
    print(
        f'Task A Accuracy after initial training: {acc_A_naive_initial * 100:.2f}%'
    )

    loss_B_naive = naive_model.train_task(
        X_B, y_B, epochs=50, lr=0.05, ewc_lambda=0.0
    )
    acc_A_naive_after = np.mean(naive_model.predict(X_A) == y_A)
    acc_B_naive_final = np.mean(naive_model.predict(X_B) == y_B)
    print(
        f'Task A Accuracy AFTER training Task B: {acc_A_naive_after * 100:.2f}% (CATASTROPHIC FORGETTING!)'
    )
    print(
        f'Task B Accuracy AFTER training Task B: {acc_B_naive_final * 100:.2f}%'
    )

    # --- EXPERIMENT 2: EWC Regularized Sequential Fine-Tuning (lambda = 50.0) ---
    print('\n[REGIME 2] Running EWC Regularized Fine-Tuning (lambda = 50.0)...')
    ewc_model = ContinualLearningEngine(layer_sizes=[8, 32, 16, 2])

    loss_A_ewc = ewc_model.train_task(X_A, y_A, epochs=50, lr=0.05)
    acc_A_ewc_initial = np.mean(ewc_model.predict(X_A) == y_A)

    # Compute Fisher Information Matrix for Task A
    ewc_model.compute_fisher_information(X_A, y_A)

    loss_B_ewc = ewc_model.train_task(
        X_B, y_B, epochs=50, lr=0.05, ewc_lambda=50.0
    )
    acc_A_ewc_after = np.mean(ewc_model.predict(X_A) == y_A)
    acc_B_ewc_final = np.mean(ewc_model.predict(X_B) == y_B)
    print(
        f'Task A Accuracy AFTER training Task B: {acc_A_ewc_after * 100:.2f}% (MEMORY RETAINED!)'
    )
    print(f'Task B Accuracy AFTER training Task B: {acc_B_ewc_final * 100:.2f}%')

    # --- 3. GENERATE COMPARATIVE PLOTS FOR PROJECT REPORT ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Accuracy Retention Bar Chart
    labels = ['Task A (Initial)', 'Task A (After Task B)', 'Task B (Final)']
    naive_scores = [
        acc_A_naive_initial * 100,
        acc_A_naive_after * 100,
        acc_B_naive_final * 100,
    ]
    ewc_scores = [
        acc_A_ewc_initial * 100,
        acc_A_ewc_after * 100,
        acc_B_ewc_final * 100,
    ]

    x = np.arange(len(labels))
    width = 0.35

    axes[0].bar(
        x - width / 2,
        naive_scores,
        width,
        label='Naive Fine-Tuning (λ=0)',
        color='#d9534f',
    )
    axes[0].bar(
        x + width / 2,
        ewc_scores,
        width,
        label='EWC Regularized (λ=50)',
        color='#5cb85c',
    )
    axes[0].set_ylabel('Accuracy (%)', fontsize=12)
    axes[0].set_title(
        'Accuracy Retention: Naive vs. EWC Fine-Tuning',
        fontsize=13,
        fontweight='bold',
    )
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(labels, fontsize=10)
    axes[0].set_ylim([0, 105])
    axes[0].legend(fontsize=10)
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Plot 2: Training Loss Curves on Task B
    axes[1].plot(
        loss_B_naive,
        label='Naive Task B Loss (λ=0)',
        color='#d9534f',
        linewidth=2,
    )
    axes[1].plot(
        loss_B_ewc,
        label='EWC Task B Total Loss (λ=50)',
        color='#0275d8',
        linewidth=2,
    )
    axes[1].set_xlabel('Epochs', fontsize=12)
    axes[1].set_ylabel('Total Cross-Entropy Loss', fontsize=12)
    axes[1].set_title(
        'Task B Loss Trajectory during Fine-Tuning',
        fontsize=13,
        fontweight='bold',
    )
    axes[1].legend(fontsize=10)
    axes[1].grid(linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('ewc_results_comparison.png', dpi=300)
    print('\n[INFO] Experimental comparison chart saved to: ewc_results_comparison.png')
    plt.show()


if __name__ == '__main__':
    run_continual_learning_experiment()