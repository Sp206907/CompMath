import numpy as np

def runde(f, x0, y0, x_end, h):
    steps = int(np.round((x_end - x0) / h))
    x = np.linspace(x0, x_end, steps + 1)
    y = np.zeros(steps + 1)
    y[0] = y0

    for i in range(steps):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
        k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y

def func_rk(x, y):
    return x ** 2 + y ** 2

x_rk, y_rk = runde(func_rk, x0=1.0, y0=1.2, x_end=1.05, h=0.05)
print(f"x={x_rk[-1]:.2f}): {y_rk[-1]:.5f}")