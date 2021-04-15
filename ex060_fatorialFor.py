numero = int(input('Digite um número: '))
fat = numero
for i in range(1, numero):
    fat *= i
print(fat)

# fatorial com biblioteca
from math import factorial
fator = factorial(numero)
print(fator)

