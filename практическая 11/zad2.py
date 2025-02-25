a = "(a + b) * (c - d)"

b = 0

for i in a:
    if i == '(':
        b += 1
    elif i == ')':
        b -= 1
    if b < 0:
        print(False)
        break
else:
    print(b == 0)
