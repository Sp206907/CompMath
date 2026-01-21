from scipy.interpolate import CubicSpline

x_vals = [1, 2, 3, 4, 5]
y_vals = [32, 17, 34, 20, 27]

f_spline = CubicSpline(x_vals, y_vals, bc_type='natural')

result = f_spline(2.5)

print(f" f(2.5): {result:.4f}")