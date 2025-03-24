import math


def task2(x):
    try:
        a = math.sin(x)
        if a <= 0:
            return "Ошибка: значение под логарифмом не может быть  равно нулю."
        y = math.log(math.sqrt(a / (5 * x + 4)) * math.exp(x)) + math.sqrt(a / (x ** 2 + 1))
        return y
    except ValueError as e:
        return "Ошибка при вычислениях: {}".format(e)


def get_input():
    while True:
        try:
            x_value = float(input("Введите значение x: "))
            return x_value
        except ValueError:
            print("Ошибка: введено некорректное значение. Пожалуйста, введите число.")


if __name__ == "__main__":
    while True:
        x_value = get_input()
        result = task2(x_value)

        if "Ошибка" in str(result):
            print(result)
        else:
            print("Результат задачи 2 (y): {}".format(result))
            break 