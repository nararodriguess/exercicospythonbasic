somaIdade= 0
idadeHomemVelho = 0
homemVelho = ''
mulheresNovas = 0
for i in range(1,5):
    nome = str(input(f'Digite o nome da {i}ª pessoa: '))
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}ª pessoa: [M/F]'))
    if idade > idadeHomemVelho and sexo in 'Mm':
        idadeHomemVelho = idade
        homemVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresNovas += 1
    somaIdade += idade
print(f'A média das idades é {somaIdade/4}.')
print(f'O homem mais velho é {homemVelho} com {idadeHomemVelho}.')
print(f'Há {mulheresNovas} mulher(es) com menos de 20 anos')