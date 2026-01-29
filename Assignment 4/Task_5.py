from scipy.interpolate import CubicSpline

x_vals = [1, 2, 3, 4, 5]
y_vals = [32, 17, 34, 20, 27]

f_spline = CubicSpline(x_vals, y_vals, bc_type='natural')#This "Edge Brick" tells the curve to stop bending and go straight at the very ends.
#This brick does the heavy lifting.
# It solves a giant math puzzle (system of equations) to ensure that the "joints" between curves are invisible.

result = f_spline(2.5) #This is the "Evaluation Brick."
# It finds which two points $2.5$ is between and uses the specific local formula for that gap.

print(f" f(2.5): {result:.4f}")