import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_13_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpson_38_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (3 * h / 8) * (y[0] + 3 * (np.sum(y[1:-1]) - np.sum(y[3:-1:3])) + 2 * np.sum(y[3:-3:3]) + y[-1])

def booles_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4 for Boole's rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    # Weights for Boole's: 7, 32, 12, 32, 7 (repeated)
    sum_val = 7 * (y[0] + y[-1])
    for i in range(1, n):
        if i % 4 == 0: sum_val += 14 * y[i]
        elif i % 2 == 0: sum_val += 12 * y[i]
        else: sum_val += 32 * y[i]
    return (2 * h / 45) * sum_val

def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6 for Weddle's rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    # Weights for Weddle's: 1, 5, 1, 6, 1, 5, 2...
    sum_val = 0
    for i in range(0, n, 6):
        sum_val += (3*h/10) * (y[i] + 5*y[i+1] + y[i+2] + 6*y[i+3] + y[i+4] + 5*y[i+5] + y[i+6])
    return sum_val

# Example Usage:
f = lambda x: 1 / (1 + x**2)  # Integral of this from 0 to 1 is pi/4
a, b = 0, 1
n = 12 # Multiple of 2, 3, 4, and 6 to satisfy all rules

print(f"Trapezoidal:  {trapezoidal_rule(f, a, b, n):.10f}")
print(f"Simpson 1/3:  {simpson_13_rule(f, a, b, n):.10f}")
print(f"Simpson 3/8:  {simpson_38_rule(f, a, b, n):.10f}")
print(f"Boole's:      {booles_rule(f, a, b, n):.10f}")
print(f"Weddle's:     {weddles_rule(f, a, b, n):.10f}")
print(f"Exact (pi/4): {np.pi/4:.10f}")