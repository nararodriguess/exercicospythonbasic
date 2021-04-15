listaNome = []
listaIdade = []
listaSexo = []
somamedia = 0
for i in range(1, 5):
    nome = str(input(f'Digite o nome da {i}ª pessoa: ')).lower()
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = int(input(f'Digite o sexo da {i}ª pessoa: '))
    listaNome.append(nome)
    listaSexo.append(sexo)
    listaIdade.append(idade)
    somamedia += idade
print('-'*50)
print(f'\nA média das idades é de {somamedia / 4}')

maiorIdade = 0
homemVelho = ''
for c in range(0,4):
    if listaIdade[c] > maiorIdade:
        if listaSexo[c] == 2:
            homemVelho = listaNome[c]
            maiorIdade = listaIdade[c]
if homemVelho == '':
    print('Não há homens na amostra')
else:
    print(f'O homem mais velho é {homemVelho.title()} com {maiorIdade} anos')

mulherNova = 0
for b in range(0,4):
    if listaIdade[b] < 20:
        if listaSexo[b] == 1:
            mulherNova += 1
print(f'Há {mulherNova} mulher(es) com menos de 20 anos em sua amostra')