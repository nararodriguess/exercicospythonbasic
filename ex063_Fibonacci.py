numero = int(input('Quantos termos você quer mostrar: '))
termoa = 0
termob = 1
cont = 0
print(f'{termoa}, {termob}', end=', ')
while cont < numero-2:
    termoc = termoa + termob
    print(termoc, end=', ')
    termoa = termob
    termob = termoc
    cont += 1
print('FIM')
