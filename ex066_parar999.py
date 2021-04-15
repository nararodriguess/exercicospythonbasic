soma = cont = 0
while True:
    n = int(input('Digit um valor ( 999 para parar): '))
    if n ==999:
        break
    else:
        cont += 1
        soma += n
print(f'Você digitou {cont} números e a soma é {soma}')