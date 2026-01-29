def divided_differences(x_nodes, y_nodes, x_target):
    n = len(y_nodes)
    table = [[0] * n for _ in range(n)]
    for i in range(n): table[i][0] = y_nodes[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_nodes[i + j] - x_nodes[i])
            #This is the "Slope Brick." Instead of just subtracting $y$, we divide by the distance between $x$ points.
            # This calculates the "steepness" or "velocity" between points.

    result = table[0][0]
    product = 1
    for i in range(1, n):
        product *= (x_target - x_nodes[i - 1])
        #We keep multiplying $(x - x_0), (x - x_1) \dots$ as we move through the formula.
        result += table[0][i] * product
    return result


x4 = [2, 2.5, 3, 3.5, 4]
y4 = [val ** 3 - val + 1 for val in x4]
print(f"Task_4: f(3.8) = {divided_differences(x4, y4, 3.8)}")