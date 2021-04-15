soma = 0
cont = 0
# MODELO DE CONTAGEM 01
for c in range(1, 501):
    if 0 != c % 2 and 0 == c % 3:
        soma += c
        cont += 1

# MODELO DE CONTAGEM 02
for c in range(1, 501, 2):
    if 0 == c % 3:
        print(c, end=' ')

print(f'\n{soma} é a soma de {cont} valores')
