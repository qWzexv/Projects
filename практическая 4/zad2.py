import math

n = int(input("Введите натуральное число n: "))

wer = 0
for i in range(1, n + 1):
    wer += (i + 1) / i

print("Результат выражения: ", wer)