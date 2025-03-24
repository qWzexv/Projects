import math


def formyla1(x):
    a = math.sin(x)
    try:
        z = math.sqrt(math.sin(x) / (x ** 2 + 4)) + math.sin(abs(a ** 4))
        return z
    except ValueError:
        return "Ошибка: невозможно вычислить квадратный корень."


while True:
    try:

        x_value = float(input("Введите значение x для задачи 1: "))

        result = formyla1(x_value)

        if isinstance(result, str) and "Ошибка" in result:
            print(result)
            continue
        print("Результат задачи 1 (z): {}".format(result))
        break

    except ValueError:
        print("Ошибка: введено некорректное значение для x. Попробуйте снова.")