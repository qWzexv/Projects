n = 3  
a = 2 * n 


b = [[0 for _ in range(a)] for _ in range(a)]

c = 1
for i in range(a):
    for j in range(a):
        b[i][j] = c
        c += 1

for wer in b:
    print(wer)
