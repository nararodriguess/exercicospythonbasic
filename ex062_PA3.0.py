print('=-='*6)
print('\033[31mCALCULANDO UMA PA\033[m')
print('=-='*6)

numero = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
termos = 10
mais = termos
while mais != 0:
    while termos != 0:
        print(numero, end=', ')
        numero = numero + razao
        termos -=1
    mais = int(input('Quantos termos deseja ver a mais? '))
    termos += mais
print('FIM')
