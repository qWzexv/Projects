import math

try:
    n = int(input("Введите размер матрицы n (n x n): "))
    
    
    if n <= 0:
        raise ValueError("Размер матрицы должен быть положительным числом.")
    
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            F[i][j] = round(2 * math.sin(math.sqrt(i + 2 * j)), 1)

    if n >= 4:  
        col4 = 1
        for i in range(n):
            col4 *= F[i][3] 
    else:
        col4 = None

    
    if n >= 2: 
        sum_row2 = sum(F[1]) 
    else:
        sum_row2 = None
    cont = sum(1 for row in F for elem in row if elem < 0)

    print("Матрица F:")
    for row in F:
        print(row)
    print("Произведение элементов четвертого столбца:", col4)
    print("Сумма элементов второй строки:", sum_row2)
    print("Количество отрицательных элементов в матрице:", cont)

except ValueError as e:
    print("Ошибка ввода:", e)
except Exception as e:
    print("Произошла ошибка:", e)
