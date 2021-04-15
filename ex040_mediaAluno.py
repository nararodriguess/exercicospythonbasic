n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2

if media < 5:
    print(f'\033[0:31mREPROVADO!\033[m Média do aluno é {media}.')
elif 5 <= media < 7:
    print(f'\033[0:33mRECUPERAÇÃO!\033[m Média do aluno é {media}.')
else:
    print(f'\033[0:32mAPROVADO!\033[m Média o aluno é {media}.')
