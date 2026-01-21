def newton_forward(x_nodes, y_nodes, x_target):
    n = len(y_nodes)
    diff = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diff[i][0] = y_nodes[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]

    h = x_nodes[1] - x_nodes[0]
    u = (x_target - x_nodes[0]) / h

    result = diff[0][0]
    u_product = 1
    factorial = 1

    for i in range(1, n):
        u_product *= (u - (i - 1))
        factorial *= i
        result += (u_product * diff[0][i]) / factorial

    return result


x_data = [1, 2, 3, 4]
y_data = [1, 3, 8, 16]
print(f"Result f(1.5): {newton_forward(x_data, y_data, 1.5)}")