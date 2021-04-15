n = int(input('Digite o número a ser convertido: '))
print('''Escolha uma das seguintes opções: 
\t [ 1 ] Binário
\t [ 2 ] Octal
\t [ 3 ] Hexadecimal''')
opcao = int(input())
if opcao == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif opcao ==2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Erro! Dados inválidos')
