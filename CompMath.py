import numpy as np

def solve_cramer(A,B):
    det_A = np.linalg.det(A)
    if det_A < 1e-9:
        return "The has no unique solution"
    n = len(B)
    results=[]
    for i in range(n):
        A_temp = A.copy()
        A_temp[:,i] = B
        det_A_temp = np.linalg.det(A_temp)
        results.append(det_A_temp/det_A)
    return np.array(results)
A = np.array([[3, -2], [1, 4]])
B = np.array([5, 11])
print(solve_cramer(A,B))

import numpy as np


def gaussian_elimination(C, D):
    C = C.astype(np.float64)
    D = D.astype(np.float64)
    n = len(D)

    # Fix: Ensure D is a column vector before hstack
    augmented = np.hstack([C, D.reshape(-1, 1)])

    # --- Step 1: Forward Elimination ---
    for i in range(n):
        for j in range(i + 1, n):
            multiplier = augmented[j, i] / augmented[i, i]
            # Row_j = Row_j - multiplier * Row_i
            augmented[j, i:] = augmented[j, i:] - multiplier * augmented[i, i:]

    # --- Step 2: Back-Substitution ---
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # x_i = (constant - sum(coefficients * known_x)) / diagonal_coefficient
        sum_val = np.dot(augmented[i, i + 1:n], x[i + 1:n])
        x[i] = (augmented[i, n] - sum_val) / augmented[i, i]

    return x


C = np.array([[6.5, 2.2, 3.0, 2.8],
              [4.0, 3.2, 1.2, 4.3],
              [3.2, 3.3, 4.0, 2.0],
              [4.6, 3.4, 1.1, 3.8]])
D = np.array([1.6, 4.0, 4.5, 3.2])

print("Solution x1, x2, x3, x4:")
print(gaussian_elimination(C, D))

import numpy as np


def gauss_jordan(E, F):
    # Combine into augmented matrix
    M = np.hstack([E.astype(float), F.astype(float).reshape(-1, 1)])
    n, m = M.shape

    for i in range(n):
        # 1. Normalize the pivot row (make the diagonal element 1)
        pivot = M[i, i]
        if pivot != 0:
            M[i] = M[i] / pivot

        # 2. Eliminate all other entries in this column (above and below)
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j, i] * M[i]
    return M


# Data from Problem 3 (4 eq, 5 vars - note the 0 column for x4 in some eqs)
E = np.array([
    [2, 2, -1, 0, 1],
    [-1, -1, 2, -3, 1],
    [1, 1, -2, 0, -1],
    [0, 0, 1, 1, 1]
])
F = np.array([0, 0, 0, 0])

print("Gauss-Jordan Reduced Row Echelon Form:")
print(gauss_jordan(E, F))

import numpy as np


def jacobi_method(V, y, x_init, iterations):
    n = len(y)
    x = x_init.copy()

    for k in range(iterations):
        x_new = np.zeros(n)
        for i in range(n):
            # Sum of A[i,j] * x_old[j] for all j except i
            s = sum(V[i, j] * x[j] for j in range(n) if i != j)
            x_new[i] = (y[i] - s) / V[i, i]
        x = x_new
        print(f"Iteration {k + 1}: x={x[0]:.4f}, y={x[1]:.4f}, z={x[2]:.4f}")
    return x

# Define Matrix A and Vector b
V = np.array([[4, 1, 1],
              [1, 5, 2],
              [1, 2, 6]], dtype=float)
y = np.array([7, 10, 14], dtype=float)
initial_guess = np.array([0, 0, 0], dtype=float)

# Execute
jacobi_method(V, y, initial_guess, iterations=3)

import numpy as np


def gauss_seidel(X, g, x_init, iterations=3):
    n = len(g)
    x = x_init.copy()

    for k in range(iterations):
        for i in range(n):
            # Sum of A[i,j] * x[j]
            # Because we update x[i] directly in the loop,
            # the next variable calculation will use this updated value.
            s = sum(X[i, j] * x[j] for j in range(n) if i != j)
            x[i] = (g[i] - s) / X[i, i]

        print(f"Iteration {k + 1}: x={x[0]:.4f}, y={x[1]:.4f}, z={x[2]:.4f}")
    return x


# System Data
X = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 6]], dtype=float)
g = np.array([7, 10, 14], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

gauss_seidel(X, g, x0)

import numpy as np


def relaxation_method(S, w, omega, iterations):
    n = len(w)
    x = np.zeros(n)

    for k in range(iterations):
        for i in range(n):
            # Gauss-Seidel sum
            s = sum(S[i, j] * x[j] for j in range(n) if i != j)
            # The SOR update formula
            x[i] = (1 - omega) * x[i] + (omega / S[i, i]) * (w[i] - s)

        print(f"Iteration {k + 1}: x={x[0]:.4f}, y={x[1]:.4f}, z={x[2]:.4f}")


# Data
S = np.array([[3, 1, -1], [1, 4, 1], [-1, 1, 5]], dtype=float)
w = np.array([3, 6, 7], dtype=float)

relaxation_method(S, w, omega=1.2, iterations=3)