print('''\tTABUADA''')
numero = int(input('Digite um número: '))
print('-'*50)
print('{:^9} {:^10} {:^10} {:^14}'.format('Soma', 'Subtração', 'Multiplicação', 'Divisão'))
print('-'*50)
for c in range (1,11):
    print(f'{numero:}+{c:^2}= {numero+c}\t', end='')
    print(f'{numero:}-{c:^2}= {numero-c:^2}\t', end='')
    print(f'{numero:}x{c:^2}= {numero*c:^2}\t', end= '')
    print(f'{numero:}/{c:^2}= {numero/c:.2f}')

