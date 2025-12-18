import math

def f(x):
    return math.exp(x) - x**2

def df(x):
    return math.exp(x) - 2*x
def bisection(a, b, eps=1e-6):
    if f(a)*f(b) >= 0:
        print("root not in diapozon")
        return None

    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


root_bis = bisection(-1, 0)
print("Bisection:", root_bis)
def fixed_point(x0, eps=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = -math.sqrt(math.exp(x))
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x


root_fp = fixed_point(-1)
print("Fixed-point:", root_fp)
def newton(x0, eps=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x


root_newton = newton(-1)
print("Newton-Raphson:", root_newton)
def secant(x0, x1, eps=1e-6, max_iter=100):
    for _ in range(max_iter):
        if f(x1) - f(x0) == 0:
            return x1
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        if abs(x2 - x1) < eps:
            return x2
        x0, x1 = x1, x2
    return x1


root_sec = secant(-1, 0)
print("Secant:", root_sec)
def false_position(a, b, eps=1e-6, max_iter=100):
    if f(a)*f(b) >= 0:
        print("root not in diapozon")
        return None

    for _ in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < eps:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c


root_fp2 = false_position(-1, 0)
print("False position:", root_fp2)
def muller(x0, x1, x2, eps=1e-6, max_iter=100):
    for _ in range(max_iter):
        h1 = x1 - x0
        h2 = x2 - x1
        δ1 = (f(x1) - f(x0)) / h1
        δ2 = (f(x2) - f(x1)) / h2
        d = (δ2 - δ1) / (h2 + h1)

        b = δ2 + h2*d
        D = math.sqrt(b*b - 4*f(x2)*d)

        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2*f(x2)/E
        x3 = x2 + h

        if abs(h) < eps:
            return x3

        x0, x1, x2 = x1, x2, x3

    return x2


root_mul = muller(-1, -0.5, 0)
print("Muller:", root_mul)
