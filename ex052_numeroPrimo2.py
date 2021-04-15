numero = int(input('Digite um número: '))
cont = 0
for i in range(1,numero+1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} foi dividido {cont} vezes, por isso não é primo')