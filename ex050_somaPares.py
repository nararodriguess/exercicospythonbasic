soma = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}° numero: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos numeros pares é {soma}')
