import math
a = int(input("Введите натуральное число: "))
b = str(a)
if b == b[::-1]:
    print(a, "является палиндромом.")
else:
    print(a, "не является палиндромом.")