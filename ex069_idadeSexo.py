print('-'*5, 'Cadastro', '-'*5)
mulhermenor = maioridade = homens = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
    if 'F' in sexo:
        if idade < 20:
            mulhermenor+=1
    if idade > 18:
        maioridade += 1
    if 'M' in sexo:
        homens += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? ')).upper().strip()[0]
    if 'N' in continua:
        break
print('='*5, 'ESTATÍSTICAS', '='*5)
print(f'''O total de mulheres com menos de 20 anos é {mulhermenor}.
O total de pessoas maiores de 18 anos é {maioridade}.
O total de homens é {homens}.''')
