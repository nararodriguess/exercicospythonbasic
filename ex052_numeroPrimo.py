numero = int(input('Digite um número: '))
primo = 'não é primo'
for i in range(2, numero+1):
    if numero == 2 or numero % i != 0:
        primo = 'é primo'
        break
    elif numero % i == 0:
        primo = 'não é primo'
        break
print(f'Numero {primo}')
