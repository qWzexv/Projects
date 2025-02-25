n = int(input("Введите натуральное число n: "))
wer = str(n)

a = set()
b = False
for i in wer:
    if i in a:
        b = True
        break
    a.add(i)
if b:
    print("Цифры в числе не все различны.")
else:
    print("Все цифры в числе различны.")
