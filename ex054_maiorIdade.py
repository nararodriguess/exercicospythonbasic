from datetime import date
anoAtual = date.today().year
cont = 0
for i in range(1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    if anoAtual - anoNascimento >= 21:
        cont +=1
print(f'Nessa relação temos {cont} pessoa maiores de idade e {7-cont} menores de idade')