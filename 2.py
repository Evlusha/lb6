import random

# Функция для генерации случайного числа в заданном диапазоне
def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Функция для создания и инициализации матрицы
def create_matrix(m):
    matrix = []
    for _ in range(m):
        row = [get_random_number(-100, 100) for _ in range(m)]
        matrix.append(row)
    return matrix

# Функция для вывода матрицы на экран
def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

# Функция для сортировки столбцов матрицы
def sort_columns(matrix):
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        if j % 2 == 0:
            column.sort()
        else:
            column.sort(reverse=True)
        for i in range(len(matrix)):
            matrix[i][j] = column[i]

# Функция для подсчета положительных элементов в верхней и нижней половинах матрицы
def count_positive_elements(matrix):
    m = len(matrix)
    upper_half_positives = 0
    lower_half_positives = 0
    for i in range(m):
        for j in range(m):
            if i < j: # Верхняя половина
                if matrix[i][j] > 0:
                    upper_half_positives += 1
            elif i == j: # Главная диагональ
                if matrix[i][j] > 0:
                    upper_half_positives += 1
                    lower_half_positives += 1
            else: # Нижняя половина
                if matrix[i][j] > 0:
                    lower_half_positives += 1

    if lower_half_positives > upper_half_positives:
        print(f"В нижней половине матрицы больше положительных элементов. {lower_half_positives} > {upper_half_positives}")
    elif lower_half_positives < upper_half_positives:
        print(f"В верхней половине матрицы больше положительных элементов. {lower_half_positives} < {upper_half_positives}")
    else:
        print(f"Количество элементов в верхней и нижней половине одинаково. {lower_half_positives} = {upper_half_positives}")

def user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 5:
                raise ValueError("Порядок матрицы должен быть больше 5.")
            return value
        except ValueError as e:
            print("Ошибка:", e)

def main():
    m = user_input("Введите порядок квадратной матрицы: ")
    matrix = create_matrix(m)

    print("Исходная матрица:")
    print_matrix(matrix)

    # Сортировка столбцов
    sort_columns(matrix)

    print("Матрица после сортировки:")
    print_matrix(matrix)

    # Подсчет положительных элементов в каждой половине матрицы
    count_positive_elements(matrix)

if __name__ == "__main__":
    main()
