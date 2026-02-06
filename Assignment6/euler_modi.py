import numpy as np

def modified_euler(f, x0, y0, x_end, h):
    steps = int(np.round((x_end - x0) / h))
    x = np.linspace(x0, x_end, steps + 1)
    y = np.zeros(steps + 1)
    y[0] = y0

    for i in range(steps):
        y_pred = y[i] + h * f(x[i], y[i])
        slope_start = f(x[i], y[i])
        slope_end = f(x[i + 1], y_pred)
        y[i + 1] = y[i] + (h / 2.0) * (slope_start + slope_end)
    return x, y

x_me, y_me = modified_euler(func_euler, x0=0, y0=1, x_end=1.0, h=0.1)
print(f"x={x_me[-1]:.2f}): {y_me[-1]:.5f}")