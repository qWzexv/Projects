from input import visov

def main():
    A = [1, 2, 3, 4, 5, 2, 6]
    znach = 2
    B = visov(A, znach)
    print("Исходный список A:", A)
    print("Значение для исключения:", znach)
    print("Отфильтрованный список B:", B)
if __name__ == "__main__":
    main()