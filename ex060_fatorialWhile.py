numero = int(input('Digite um número: '))
cont = 1
fat = numero
while cont != numero:
    fat *= cont
    cont += 1
print(f'O fatorial de {numero} é {fat}')
