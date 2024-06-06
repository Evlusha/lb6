import numpy as np 

def calculate_new_value(i, matrix, reply, x):
    sum1 = sum(matrix[i][j] * x[j] for j in range(i))
    sum2 = sum(matrix[i][j] * x[j] for j in range(i + 1, len(matrix)))
    return (reply[i] - sum1 - sum2) / matrix[i][i]

def solve_system(matrix, reply, x, epsilon, max_iterations):
    n = len(matrix)
    x_new = np.zeros(n)
    iterations = 0

    print("|-----|----------|----------|----------|----------|-------------|")
    print("|  N  |    x1    |    x2    |    x3    |    x4    |   Epsilon   |")
    print("|-----|----------|----------|----------|----------|-------------|")

    while iterations < max_iterations:
        max_diff = 0
        for i in range(n):
            old_value = x_new[i]
            x_new[i] = calculate_new_value(i, matrix, reply, x_new)
            max_diff = max(max_diff, abs(x_new[i] - old_value))
        print(f"|  {iterations:3d}  | {x_new[0]:8.4f} | {x_new[1]:8.4f} | {x_new[2]:8.4f} | {x_new[3]:8.4f} | {epsilon:11.4f} |")
        if max_diff < epsilon:
            print("|-----|----------|----------|----------|----------|-------------|")
            print(f"\nКоличество итераций:  {iterations}")
            break
        iterations += 1

    print("Решение:")
    for i in range(n):
        print(f"x{i + 1} = {x_new[i]:.4f}")

def output(matrix, reply):
    print("Канонический вид:")
    variables = ['a', 'b', 'c', 'd']
    for i in range(len(matrix)):
        row = " + ".join(f"{matrix[i][j]:8.3f}*{variables[j]}" for j in range(len(matrix[i])))
        print(f"{row} = {reply[i]:.3f}")
    print()

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i, n):
            sum_value = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_value
        
        for j in range(i, n):
            if i == j:
                L[i][j] = 1
            else:
                sum_value = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - sum_value) / U[i][i]

    print("Матрица U:")
    print(U)

    print("Матрица L:")
    print(L)

    return L, U

def forward_substitution(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

def main():
    M = -1.21
    N = 0.2
    P = 0.88
    epsilon = 0.001
    max_iterations = 1000

    A = np.array([
        [M, -0.04, 0.21, -18],
        [0.25, -1.23, N, -0.09],
        [-0.21, N, 0.8, -0.13],
        [0.15, -1.31, 0.06, P]
    ])

    b = np.array([-1.24, P, 2.56, M])

    L, U = lu_decomposition(A)

    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

    print("Результаты прямой подстановки (нахождение y):")
    for i in range(len(y)):
        print(f"y{i + 1} = {y[i]:.4f}")

    print("Результаты обратной подстановки (нахождение x):")
    for i in range(len(x)):
        print(f"x{i + 1} = {x[i]:.4f}")

    matrix = np.array([
        [0.25, -1.23, 0.2, -0.09],
        [-0.15, 1.31, -0.06, -0.88],
        [-0.21, 0.2, 0.8, -0.13],
        [1.21, 0.04, -0.21, 18]
    ])

    reply = np.array([0.88, 1.21, 2.56, 1.24])

    output(matrix, reply)

    x1 = np.zeros(len(matrix))
    solve_system(matrix, reply, x1, epsilon, max_iterations)

if __name__ == "__main__":
    main()
