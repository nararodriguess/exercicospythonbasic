print('=-='*6)
print('\033[31mCALCULANDO UMA PA\033[m')
print('=-='*6)
numero = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <=10:
    print(numero, end = ', ')
    numero += razao
    cont +=1
print('FIM')
