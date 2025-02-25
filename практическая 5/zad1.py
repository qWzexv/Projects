import math

def process_number(N):
    i = str(N)
    if len(i) == 5:
        M = i[:2] + i[3:] 
        M = int(M) 
        return M, len(str(M)) 
    else:
        return None, None  

N = 12345
M, wer = process_number(N)
if M is not None:
    print("Новое число M: " + str(M) + ", Количество цифр в M: " + str(wer))
else:
    print("Число N не содержит 5 цифр.")
