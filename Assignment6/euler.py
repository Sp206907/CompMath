import numpy as np

def euler(f, x0, y0, x_end, h):
    steps = int(np.round((x_end - x0) / h))
    x = np.linspace(x0, x_end, steps + 1)
    y = np.zeros(steps + 1)
    y[0] = y0

    for i in range(steps):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def func_euler(x, y):
    return y

x_e, y_e = euler(func_euler, x0=0, y0=1, x_end=1.0, h=0.1)
print(f"x={x_e[-1]:.2f}): {y_e[-1]:.5f}")