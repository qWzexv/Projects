def wer(bukva):
    a = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    b = set('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ') 

    c = 0
    d = 0
    for i in bukva:
        if i in a:
            c += 1
        elif i in b:
            d += 1
    return c, d
bukva = input("Введите текст: ")
c, d = wer(bukva)

print("Количество гласных: " + str(c))
print("Количество согласных: " + str(d))

if c > d:
    print("Гласных больше.")
elif d > c:
    print("Согласных больше.")
else:
    print("Количество гласных и согласных одинаково.")
