import random
file = 'main.txt'

chislo = 10  

with open(file, 'w') as file:
    for i in range(chislo):
        randomnie = random.randint(1, 10) 
        file.write(str(randomnie) + "\n")
