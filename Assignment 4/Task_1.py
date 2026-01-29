import math
def lagrange(x_nodes, y_nodes, x_target):
    total_sum = 0 #Our bucket. We add the contribution of each point into this bucket.
    n = len(x_nodes)
    for i in range(n): #We pick up each point $(x_i, y_i)$ one by one to see how much it helps
        num, den = 1, 1 #These are the bricks for the Basis Polynomial ($L_i$). We start at 1 because we are going to multiply.
        for j in range(n):
            if i != j: #This is the "Safety Brick." #
                # If $i$ equals $j$, the bottom of our fraction becomes zero ($x_i - x_i = 0$), and the code crashes. We skip the current point to avoid this.
                num *= (x_target - x_nodes[j])
                den *= (x_nodes[i] - x_nodes[j])
        total_sum += y_nodes[i] * (num / den) #We take the "strength" of the point ($num/den$) and multiply it by the height ($y_i$).
    return total_sum

n_nodes = 6
x_nodes = [i * (2 * math.pi) / (n_nodes - 1) for i in range(n_nodes)]
y_nodes = [math.sin(x) for x in x_nodes]

z_points = [i * (2 * math.pi) / 100 for i in range(101)]
results_lagrange = [lagrange(x_nodes, y_nodes, z) for z in z_points]
results_true = [math.sin(z) for z in z_points]

print("True Sin | Lagrange | Error")
for i in range(5):
    error = abs(results_true[i] - results_lagrange[i])
    print(f"{results_true[i]:.4f} | {results_lagrange[i]:.4f} | {error:.4e}")