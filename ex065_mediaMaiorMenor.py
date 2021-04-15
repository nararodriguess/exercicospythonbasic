n = int(input('Digite um novo número: '))
continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
cont = 1
soma = maior = menor = n
while continuar in 'Ss':
    n = int(input('Digite um novo número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
print(f'A média entre os númerios digitados  é {(soma/cont):.2f}')
print(f'O maior número é {maior}, o menor é {menor}.')
