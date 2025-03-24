def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

while True:
    try:
        number = int(input("Введите натуральное число: "))
        print(f"Количество цифр в числе {number}: {count_digits(number)}")
        break
    except ValueError:
        print("Ошибка, введите корректное число.")