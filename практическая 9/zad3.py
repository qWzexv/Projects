import math

a = [1, -2, 3, -4, 5, -6, 7]

b = 0

for i in range(len(a)):
    if a[i] < 0:
        a[i], a[b] = a[b], a[i]
        b += 1

print(a)  
