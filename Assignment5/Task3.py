import numpy as np

def simpson_13_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Error: n have to be even")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    sum_odd = np.sum(y[1:-1:2])
    sum_even = np.sum(y[2:-1:2])

    integral = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])
    return integral

f = lambda x: x ** 2
a, b, n = 0, 6, 12

result = simpson_13_rule(f, a, b, n)
print(f"Simpson's 1/3 rule: {result:.4f}")