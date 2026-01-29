def newton_backward(x_nodes, y_nodes, x_target):
    n = len(y_nodes)
    diff = [[0] * n for _ in range(n)]
    for i in range(n): diff[i][0] = y_nodes[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1): #This is the "Reverse Brick." It tells Python to count backwards from the bottom of the list.
            diff[i][j] = diff[i][j - 1] - diff[i - 1][j - 1]

    h = x_nodes[1] - x_nodes[0]
    v = (x_target - x_nodes[-1]) / h #Instead of the start, we measure how many steps we are away from the last point ($x_n$).

    result = diff[n - 1][0] #We start our sum with the last $y$ value in the list
    v_product = 1
    factorial = 1

    for i in range(1, n):
        v_product *= (v + i - 1)
        factorial *= i
        result += (v_product * diff[n - 1][i]) / factorial #We only use the bottom row of our notebook.'


    return result


x3 = [-1, 0, 1, 2]
y3 = [0.5, 1.0, 2.5, 4.0]
print(f"Task 3: f(1.5) = {newton_backward(x3, y3, 1.5)}")