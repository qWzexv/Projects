import math

a = [1.5, 2.3, 4.0, 0.0, 3.7, -1.2]


b = sum(a) / len(a)

wer = max(a)
rew = min(a)

you = min(a, key=lambda x: abs(x - b))


print("Наибольший элемент:", wer)
print("Наименьший элемент:", rew)
print("Элемент, наименее удаленный от среднего арифметического:", you)
