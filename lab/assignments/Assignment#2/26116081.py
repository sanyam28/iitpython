import matplotlib.pyplot as plt
def f(x):
    return x**3-5*x
def g(x):
    return x**2+x-2

x_fx = []
x_gx = []
values_x = []
solutions = []
# selecting the range [-5,5] for the plot, reason for this specific range is that for bigger values of x fx will significantly grow bigger than gx from the value 5 difference between these two function is keep getting widened with increase in x beyond 5 safely
epsilon = 0.00001
j=-5
while j<=5:
    values_x.append(j)
    x_fx.append(f(j))
    x_gx.append(g(j))
    if ((f(j)-g(j))*(f(j+epsilon)-g(j+epsilon)))<=0:
        solutions.append(j)
    j+=epsilon
print(solutions)
plt.plot(values_x, x_fx)
plt.plot(values_x, x_gx)
plt.show()