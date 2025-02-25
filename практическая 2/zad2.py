import math

x = 1.0
y = 2.0

f = (2 ** -x) - math.cos(x) + math.sin(2 * x * y)

if x == 0:
    math.error("x не равен нулю, вычисления ")
else:
    w = (2 / math.tan(3 * x)) - (1 / (12 * x**2 + 7 * x - 5))

print(f)
print(w)
