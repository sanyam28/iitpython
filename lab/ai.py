import math
import random

# =====================================================================
# 1. MATH UTILITIES (Replicating Matrix Operations using Raw Lists)
# =====================================================================

def transpose(matrix):
    """Transposes a 2D matrix (swaps rows and columns)."""
    return [list(row) for row in zip(*matrix)]

def matmul(A, B):
    """Multiplies matrix A (m x n) by matrix B (n x p)."""
    m, n = len(A), len(A[0])
    n_B, p = len(B), len(B[0])
    if n != n_B:
        raise ValueError(f"Dimension mismatch for multiplication: {n} vs {n_B}")
    
    # Initialize empty result matrix
    result = [[0.0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0.0
            for k in range(n):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    return result

def sigmoid(x):
    """Applies sigmoid activation function to a scalar."""
    # Clip input to prevent overflow errors in raw math.exp
    x = max(-500.0, min(500.0, x))
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(activated_x):
    """Computes derivative using the already activated output: f'(x) = f(x) * (1 - f(x))."""
    return activated_x * (1.0 - activated_x)


# =====================================================================
# 2. NEURAL NETWORK CLASS
# =====================================================================

class NeuralNetworkFromScratch:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with small random values (He/Xavier approximation)
        self.W1 = [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(input_size)]
        self.W2 = [[random.uniform(-0.5, 0.5) for _ in range(output_size)] for _ in range(hidden_size)]
        
        # Initialize biases to zeros
        self.b1 = [[0.0] * hidden_size]
        self.b2 = [[0.0] * output_size]

    def forward(self, X):
        """Runs the input through the network layers."""
        self.X = X  # Store input for backpropagation
        
        # Layer 1: Hidden Layer
        # Z1 = X * W1 + b1
        self.Z1 = matmul(X, self.W1)
        for i in range(len(self.Z1)):
            for j in range(len(self.Z1[0])):
                self.Z1[i][j] += self.b1[0][j]
        # A1 = sigmoid(Z1)
        self.A1 = [[sigmoid(val) for val in row] for row in self.Z1]
        
        # Layer 2: Output Layer
        # Z2 = A1 * W2 + b2
        self.Z2 = matmul(self.A1, self.W2)
        for i in range(len(self.Z2)):
            for j in range(len(self.Z2[0])):
                self.Z2[i][j] += self.b2[0][j]
        # A2 = sigmoid(Z2)
        self.A2 = [[sigmoid(val) for val in row] for row in self.Z2]
        
        return self.A2

    def backward(self, y_true, lr=0.1):
        """Computes gradients and updates weights/biases using backpropagation."""
        m = len(y_true)  # Batch size
        
        # --- Output Layer Error & Gradients ---
        # Error = A2 - y_true
        error_output = [[self.A2[i][j] - y_true[i][j] for j in range(len(y_true[0]))] for i in range(m)]
        # dZ2 = error * sigmoid_derivative(A2)
        dZ2 = [[error_output[i][j] * sigmoid_derivative(self.A2[i][j]) for j in range(len(error_output[0]))] for i in range(m)]
        
        # dW2 = (A1^T) * dZ2
        dW2 = matmul(transpose(self.A1), dZ2)
        # db2 = sum rows of dZ2
        db2 = [[sum(dZ2[i][j] for i in range(m)) for j in range(len(dZ2[0]))]]
        
        # --- Hidden Layer Error & Gradients ---
        # dZ1 = (dZ2 * W2^T) * sigmoid_derivative(A1)
        dZ2_W2T = matmul(dZ2, transpose(self.W2))
        dZ1 = [[dZ2_W2T[i][j] * sigmoid_derivative(self.A1[i][j]) for j in range(len(dZ2_W2T[0]))] for i in range(m)]
        
        # dW1 = (X^T) * dZ1
        dW1 = matmul(transpose(self.X), dZ1)
        # db1 = sum rows of dZ1
        db1 = [[sum(dZ1[i][j] for i in range(m)) for j in range(len(dZ1[0]))]]
        
        # --- Gradient Descent Step (Weights Update) ---
        for i in range(len(self.W2)):
            for j in range(len(self.W2[0])):
                self.W2[i][j] -= lr * (dW2[i][j] / m)
                
        for i in range(len(self.W1)):
            for j in range(len(self.W1[0])):
                self.W1[i][j] -= lr * (dW1[i][j] / m)
                
        for j in range(len(self.b2[0])):
            self.b2[0][j] -= lr * (db2[0][j] / m)
            
        for j in range(len(self.b1[0])):
            self.b1[0][j] -= lr * (db1[0][j] / m)


# =====================================================================
# 3. TRAINING APPLICATION (Solving the Binary XOR Logic Gate)
# =====================================================================
if __name__ == "__main__":
    # Fix seed for reproducible results
    random.seed(42)
    
    # Dataset representing the XOR truth table
    # Inputs: [[x1, x2]]
    X_train = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
    # Expected Outputs: [[y]]
    y_train = [[0.0], [1.0], [1.0], [0.0]]
    
    # Instantiate the network: 2 inputs, 3 hidden nodes, 1 output node
    nn = NeuralNetworkFromScratch(input_size=2, hidden_size=3, output_size=1)
    
    print("--- Starting Training ---")
    epochs = 20000
    learning_rate = 0.5
    
    for epoch in range(epochs):
        # Forward pass
        predictions = nn.forward(X_train)
        
        # Backward pass & optimization
        nn.backward(y_train, lr=learning_rate)
        
        # Periodically compute and display Mean Squared Error (MSE) loss
        if epoch % 4000 == 0:
            loss = sum((predictions[i][0] - y_train[i][0])**2 for i in range(len(y_train))) / len(y_train)
            print(f"Epoch {epoch:5d} | Mean Squared Error Loss: {loss:.6f}")
            
    print("\n--- Final Predictions Evaluated After Training ---")
    final_outputs = nn.forward(X_train)
    for x, target, pred in zip(X_train, y_train, final_outputs):
        print(f"Input: {x} -> Predicted: {pred[0]:.4f} (Expected: {target[0]})")
