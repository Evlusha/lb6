import random

# Функция для создания и инициализации матрицы
def create_matrix(m, n):
    matrix = [[random.uniform(0.0, 100.0) for _ in range(n)] for _ in range(m)]
    return matrix

# Функция для вывода матрицы на экран
def print_matrix(matrix):
    print("Матрица:")
    for row in matrix:
        print("\t".join(f"{elem:.2f}" for elem in row))

# Функция для вычисления среднего арифметического значения всех элементов матрицы
def total_avg(matrix):
    total_sum = sum(sum(row) for row in matrix)
    return total_sum / (len(matrix) * len(matrix[0]))

# Функция для вычисления среднего арифметического значения каждой строки и поиска строки с максимальным значением
def row_averages(matrix):
    row_averages = [sum(row) / len(row) for row in matrix]
    max_avg_row = max(row_averages)
    max_row_index = row_averages.index(max_avg_row) + 1
    return row_averages, max_row_index

# Основная функция
def main():
    print("---Задание номер 1---")
    m = int(input("Введите количество строк: "))
    n = int(input("Введите количество столбцов: "))

    matrix = create_matrix(m, n)
    print_matrix(matrix)

    total_avg_value = total_avg(matrix)
    print(f"\nСреднее арифметическое значение всех элементов матрицы: {total_avg_value:.2f}")

    row_avg_values, max_row_index = row_averages(matrix)
    print("\nСредние арифметические значения каждой строки:")
    for i, avg in enumerate(row_avg_values, 1):
        print(f"Строка {i}: {avg:.2f}")

    print(f"\nНомер строки с наибольшим средним арифметическим значением: {max_row_index}")

if __name__ == "__main__":
    main()
