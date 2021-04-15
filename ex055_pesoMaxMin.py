lista = []
for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    lista.append(peso)
lista.sort()
print('O menor peso é {}kg e o maior é {}kg'.format(lista[0], lista[4]))