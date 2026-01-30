def newton_cotes_concept(f, a, b):
    x0, x1 = a, b
    h = b - a
    integral = (h / 2) * (f(x0) + f(x1))
    return integral

f = lambda x: x**2
print(f"Newton Cotes (basic n=1): {newton_cotes_concept(f, 0, 6):.4f}")