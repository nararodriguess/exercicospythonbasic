frase= str(input('Digite uma frase: ')).replace(' ', '').lower()
inverteFrase = frase[::-1]
print(f'O inverso de {frase} é {inverteFrase}, portanto,', end=' ')
if frase == inverteFrase:
    print('essa frase é um palidromo.')
else:
    print('essa frase não é um palidromo.')