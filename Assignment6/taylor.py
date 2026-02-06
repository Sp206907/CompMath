import numpy as np

def taylor(derivatives, x0, y0, x_end, h):
    steps = int(np.round((x_end - x0) / h))
    x_grid = np.linspace(x0, x_end, steps + 1)
    y_result = np.full_like(x_grid, y0)
    delta_x = x_grid - x0

    for k, deriv_func in enumerate(derivatives):
        order = k + 1
        d_val = deriv_func(x0, y0)
        fact = np.prod(np.arange(1, order + 1))
        term = (d_val / fact) * (delta_x ** order)
        y_result += term
    return x_grid, y_result

derivs = [
    lambda x, y: x + y,
    lambda x, y: 1 + x + y,
    lambda x, y: 1 + x + y
]

x_t, y_t = taylor(derivs, x0=0, y0=1, x_end=0.2, h=0.1)
print(f"x={x_t[-1]:.2f}): {y_t[-1]:.5f}")