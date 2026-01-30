import numpy as np

def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("Error: n have to be a multiple of 6")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = 0
    for i in range(0, n, 6):
        section = (y[i] + 5 * y[i + 1] + y[i + 2] + 6 * y[i + 3] + y[i + 4] + 5 * y[i + 5] + y[i + 6])
        integral += (3 * h / 10) * section
    return integral

f = lambda x: x ** 2
a, b, n = 0, 6, 12

result = weddles_rule(f, a, b, n)
print(f"Weddle's rule: {result:.4f}")