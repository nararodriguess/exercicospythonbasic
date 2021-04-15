print('-'*10, 'JOGO DO PAR OU IMPAR', '-'*10)
from random import randint
cont = 0
while True:
    computador = randint(0, 10  )
    usuario = int(input('Escoha um número de 0 à 10: '))
    escolha = str(input('Você escolhe PAR ou IMPAR? ')).lower().strip()[0]
    while escolha not in 'pi':
        escolha = str(input('Você escolhe PAR ou IMPAR? ')).lower().strip()[0]
    resto = (usuario + computador) % 2
    if resto == 0:
        result = 'é par'
    if resto != 0:
        result = 'é impar'
    print(f'O computador escolheu {computador} e você {usuario}')
    print('A soma entre eles é par' if resto ==0 else 'A soma entre eles é impar')
    if 'p' in escolha:
        if resto != 0:
            print(f'GAME OVER! Você acertou {cont} vez(es), continue!!!')
            break
    elif 'i' in escolha:
        if resto == 0:
            print(f'GAME OVER! Você acertou {cont} vez(es), continue!!!')
            break
    cont += 1
