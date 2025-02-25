A = [
    [3, 5, 1, 7],
    [2, 8, 4, 6],
    [9, 3, 2, 5],
    [0, 1, 6, 4],
    [7, 3, 8, 2]
]

M = len(A)
N = len(A[0]) if M > 0 else 0

wer = []
for i in range(0, M, 2):
    rew = min(A[i]) 
    wer.append(rew)

print("Наименьшие элементы каждой четной строки:")
for to, go in enumerate(wer):
    print(f"Четная строка {to * 2}: {go}")
