import math

try:
    n = int(input("Введите размер матрицы n (n x n): "))

    if n <= 0:
        raise ValueError("Размер матрицы должен быть положительным числом.")
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            F[i][j] = round(2 * math.sin(math.sqrt(i + 2 * j)), 1)
    tive_sum = 0
    cont = 0
    for i in range(n):
        for j in range(i + 1, n):  
            if F[i][j] > 0:
                tive_sum += F[i][j]
                cont += 1

    if cont > 0:
        ave = tive_sum / cont
    else:
        ave = None

    max_sum = float('-inf')
    index = -1
    for i in range(n):
        row_sum = sum(F[i])
        if row_sum > max_sum:
            max_sum = row_sum
            index = i  
    print("Матрица F:")
    for row in F:
        print(row)
    
    print("Среднее арифметическое положительных элементов выше главной диагонали:", ave)
    print("Номер первой строки с наибольшей суммой элементов:", index + 1)

except ValueError as e:
    print("Ошибка ввода:", e)
except Exception as e:
    print("Произошла ошибка:", e)
