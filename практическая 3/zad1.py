import math 
a = float(input(" стоимость книги: "))
b = float(input(" сумма  покупателем: "))
f = b - a

if f == 0:
    print("Спасибо!")
elif f > 0:
    print("Возьмите сдачу:", round(f, 2))
else:
    i = abs(f)
    print("Недостаточно средств. Не хватает:", round(i, 2))