# introdução do jogo
print('\033[33m-\033[m'*25)
import emoji
print(emoji.emojize("\t JOKÊNPO :facepunch: :hand: :v:", use_aliases=True))
print('\033[33m-\033[m'*25)

# usuario e computador escolhem seus objetos
import random
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
jogador = str(input('Pedra, papel ou tesoura? ')).strip().lower()

import time
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)
# condição para quando o usuário e o computador escolherem o mesmo objeto
while computador == jogador:
    print(f'Empatamos, você escolheu {jogador} e eu escolhi {computador} também.')
    jogador = str(input('Pedra, papel ou tesoura? ')).strip().lower()
    computador = random.choice(lista)
    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!')
    time.sleep(0.5)
# condição caso os objetos forem diferentes
else:
    if computador == 'tesoura' and jogador == 'pedra':
        print(f'Você venceu! Escolhi {computador} e você escolheu {jogador}.')
    elif computador == 'tesoura' and jogador == 'papel':
        print(f'Você perdeu! Escolhi {computador} e você escolheu {jogador}.')
    elif computador == 'papel' and jogador =='pedra':
        print(f'Você perdeu! Escolhi {computador} e você escolheu {jogador}.')
    elif computador == 'papel' and jogador == 'tesoura':
        print(f'Você venceu! Escolhi {computador} e você escolheu {jogador}.')
    elif computador =='pedra' and jogador =='papel':
        print(f'Você venceu! Escolhi {computador} e você escolheu {jogador}.')
    elif computador == 'pedra' and jogador == 'tesoura':
        print(f'Você perdeu! Escolhi {computador} e você escolheu {jogador}.')
# condição caso o usuário digite um objeto que seja diferente de pedra, papel ou tesoura.
    else:
        print('Erro! Objeto inválido.')
