frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
cont = 0
for i in range(len(frase)-1, -1, -1):
    if frase [i] == frase[cont]:
        cont += 1

if cont == len(frase):
    print('Essa frase é um paligromo')
else:
    print('Essa frase nao é um palídromo')