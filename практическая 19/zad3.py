def task3(x_values, n):
    results = []
    for x in x_values:
        S = sum(1 / (x ** i) for i in range(1, n + 1))
        results.append(S)
    return results


def get_input():
    while True:
        try:
            x_values_input = input("Введите значения x через пробел: ").split()
            x_values = [float(x) for x in x_values_input]

            n_value = int(input("Введите значение n для задачи 3: "))
            if n_value <= 0:
                print("Ошибка: n должно быть положительным целым числом.")
                continue
            return x_values, n_value
        except ValueError:
            print("Ошибка: введено некорректное значение. Пожалуйста, введите числа.")


if __name__ == "__main__":
    x_values, n_value = get_input()
    S_results = task3(x_values, n_value)

    for i, S in enumerate(S_results):
        print(f"Результат задачи 3 для x={x_values[i]}: {S}")