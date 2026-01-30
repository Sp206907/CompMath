import numpy as np

def booles_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("Error: n have to be a multiple of 4")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = 0
    for i in range(0, n, 4):
        segment = (7 * y[i] + 32 * y[i + 1] + 12 * y[i + 2] + 32 * y[i + 3] + 7 * y[i + 4])
        integral += (2 * h / 45) * segment
    return integral

f = lambda x: x ** 2
a, b, n = 0, 6, 12

result = booles_rule(f, a, b, n)
print(f"Boole's rule: {result:.4f}")