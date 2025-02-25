n = 3
wer = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for i in wer:
    print(i)
rew = wer[n - 1][:] 

you = [wer[i][n - 1] for i in range(len(wer))] 
wer[n - 1] = you
for i in range(len(wer)):
    wer[i][n - 1] = rew[i]

print("\nПреобразованная матрица:")
for i in wer:
    print(i)
