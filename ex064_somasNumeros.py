cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += n
    n = int(input('Digite mais um número: '))
print(f'PROGRAMA FINALIZADO! A soma entre os números é {cont}.')