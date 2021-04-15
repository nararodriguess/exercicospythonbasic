print('  ?  '*5)
print('\033[33mJOGO DA ADIVINHAÇÃO 2.0\033[m')
print('  ?  '*5)
from random import randint
computador = randint(0, 10)
usuario = int(input('Pensei em um número de 0 à 10. Tente adivinhar! Em qual número eu pensei? '))
cont = 1
while computador != usuario:
    if computador > usuario:
        print('Mais... Tente novamente!')
    if computador < usuario:
        print('Menos... Tente novamente!')
    usuario = int(input('Digite seu palpite: '))
    cont += 1
print(f'Parabéns, você acertou!!! Você precisou de {cont} tentativas para finalizar o jogo.')