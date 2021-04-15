print('-'*15)
print(('\tLOJINHA'))
print('-'*15)
total = contmil = cont = menor= 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        contmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = str(input('Quer continuar? ')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? ')).lower().strip()[0]
    if continuar == 'n':
        break
print(f'''O total da compra é R${total:.2f}.
Há {contmil} produtos acima de R$ 1.000,00 reais.
O produto mais barato custa R$ {menor} e é um(a) {barato}.''')
