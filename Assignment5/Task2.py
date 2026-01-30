import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

f = lambda x: x**2
a, b, n = 0, 6, 12

result = trapezoidal_rule(f, a, b, n)
print(f"Trapezoidal rule: {result:.4f}")