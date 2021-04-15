print('-'*17)
print('{:^17}'.format('MEU BANCO'))
print('-'*17)
saque = int(input('Quanto você deseja sacar: '))
cedulas = [100, 50, 20, 10, 5, 2, 1]
while True:
    print('-' * 30)
    for i in range(len(cedulas)):
        quantnotas = saque // cedulas[i]
        saque = saque % cedulas[i]
        if quantnotas != 0:
            print(f'Total de {quantnotas} notas de R${cedulas[i]} reais.')
    print('Obrigado pela preferência, tenha um bom dia!')
    break