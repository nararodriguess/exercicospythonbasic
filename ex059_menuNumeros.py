numero1 = float(input('Digite um valor: '))
numero2 = float(input('Digite outro valor: '))
menu = 0
while menu != 5:
    print('=-=' * 25)
    print(' [ 1 ] SOMAR [ 2 ] MULTIPLICAR [ 3 ] MAIOR [ 4 ] NOVOS NUMEROS [ 5 ] SAIR')
    menu = int(input('O que deseja realizar? '))
    if menu == 1:
        print(f'A soma entre {numero1} e {numero2} é {numero1 + numero2}')
    elif menu == 2:
        print(f'A mulltiplicação entre {numero1} e {numero2} é {numero1 * numero2}')
    elif menu == 3:
        if numero1 > numero2:
            print(f'O número maior é: {numero1}')
        else:
            print(f'O número maior é: {numero2}')
    elif menu == 4:
        numero1 = float(input('Digite um valor: '))
        numero2 = float(input('Digite outro valor: '))
print('Programa finalizado.')

