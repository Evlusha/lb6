import os
import time

# Размеры поля с учётом границ
width = 10
height = 10

# Функция для очистки экрана 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для отображения текущего состояния поля
def display_field(field):
    clear_screen()
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end='')  # Границы поля
            elif field[i][j] == 1:
                print("#", end='')  # Живая клетка
            else:
                print(" ", end='')  # Мертвая клетка
        print()

# Функция для вычисления следующего поколения
def next_generation(field):
    next_field = [[0] * width for _ in range(height)]
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            neighbors = sum(field[i + ni][j + nj] for ni in range(-1, 2) for nj in range(-1, 2) if not (ni == 0 and nj == 0))
            if field[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    next_field[i][j] = 0  # Смерть из-за перенаселённости или одиночества
                else:
                    next_field[i][j] = 1  # Выживание
            else:
                if neighbors == 3:
                    next_field[i][j] = 1  # Рождение новой клетки
                else:
                    next_field[i][j] = 0  # Клетка остаётся мёртвой
    return next_field

# Функция для инициализации поля
def initialize_field():
    field = [[0] * width for _ in range(height)]
    return field

# Функция для инициализации поля с шаблонами
def initialize_field_with_patterns(field):
    # Очистка поля перед установкой планера
    for i in range(height):
        for j in range(width):
            field[i][j] = 0
    # Установка планера на поле
    field[2][3] = field[3][4] = field[4][2] = field[4][3] = field[4][4] = 1  # Планер

def main():
    # Инициализация поля
    field = initialize_field()

    # Инициализация с определенными шаблонами
    initialize_field_with_patterns(field)

    generation_count = 0  # Счётчик поколений

    # Анимация
    for generation in range(100):
        display_field(field)
        if generation_count == 13:
            initialize_field_with_patterns(field)  # Обновляем планер
            generation_count = 0  # Сбрасываем счётчик поколений
        else:
            field = next_generation(field)  # Вычисляем следующее поколение
            generation_count += 1  # Увеличиваем счётчик поколений
        time.sleep(0.1)  # Задержка в секундах

if __name__ == "__main__":
    main()
