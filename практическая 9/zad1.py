import math

a = [1.5, 2.3, 4.0, 0.0]
b = 0

for i in a:
    b += 1
    if i == 0:
        break

print("Количество членов в последовательности:", b)