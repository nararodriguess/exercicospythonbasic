print('='*22)
print('PROGRESSÃO ARITMETICA')
print('='*22)
numero = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = numero + (10 - 1) * razao
print('Os dez primeiros termos da PA são: ')
for c in range(numero, termo+1, razao):
    print(c, end=', ')
