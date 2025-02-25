import math

a = float(input("Введите значение x: "))

if a <= 1:
    i = 0
else:
    i = 1 / (a + 6)
print(str(a) + " = " + str(i))