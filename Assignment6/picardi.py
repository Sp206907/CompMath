import numpy as np

def picard(f, x0, y0, x_end, h, iterations):
    steps = int(np.round((x_end - x0) / h))
    x_grid = np.linspace(x0, x_end, steps + 1)
    y_grid = np.full_like(x_grid, y0)

    for i in range(iterations):
        integrand = f(x_grid, y_grid)
        trapezoids = (integrand[:-1] + integrand[1:]) / 2 * h
        integral_values = np.cumsum(trapezoids)
        integral_values = np.concatenate(([0], integral_values))
        y_grid = y0 + integral_values
    return x_grid, y_grid

def func(x, y):
    return x + y

x_p, y_p = picard(func, x0=0, y0=1, x_end=0.2, h=0.01, iterations=3)
print(f"x={x_p[-1]:.2f}): {y_p[-1]:.5f}")