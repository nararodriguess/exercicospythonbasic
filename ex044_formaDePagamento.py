print('{:.^40}'.format('Lojas 123'))
print(' ')
preco = float(input('Digite o preço do produto: R$ '))
condicaoPagamento = str(input('''Formas de pagamento: 
\t [ 1 ] dinheiro/cheque
\t [ 2 ] cartão 1x
\t [ 3 ] cartão 2x
\t [ 4 ] cartão 3x ou mais
Digite a forma de pagamento escolhida: ''')).strip()

if condicaoPagamento == '1':
    preco2 = preco * 0.9
elif condicaoPagamento == '2':
    preco2 = preco * 0.95
elif condicaoPagamento == '3':
    preco2 = preco
    print(f'Sua compra vai ser cobrada em 2x de R${preco2/2} sem juros')
elif condicaoPagamento == '4':
    preco2 = (preco*1.2)
    parcela = int(input('Digite o número de parcelas: '))
    print(f'Sua compra vai ser cobrada {parcela}x de R${preco2/parcela} reais')
else:
    preco2 = preco
    print('\033[31mErro. Digite dados válidos!\033[m')

print(f'Sua compra de R$ {preco} reais vai custar R$ {preco2:.2f} reais.')