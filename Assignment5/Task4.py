import numpy as np

def simpson_38_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Error: n have to be a multiple of 3")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * y[i]
        else:
            integral += 3 * y[i]

    return (3 * h / 8) * integral

f = lambda x: x ** 2
a, b, n = 0, 6, 12

result = simpson_38_rule(f, a, b, n)
print(f"Simpson's 3/8 rule: {result:.4f}")