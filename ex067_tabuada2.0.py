print('-'*12)
print('TABUADA 2.0')
print('-'*12)
while True:
    n = int(input('A tabuada de qual número você quer ver? '))
    if n <= 0:
        print('Tabuada finalizada! Volte sempre')
        break
    else:
        for c in range (1, 11):
            print(f'{n} + {c:^2} = {(n+c):^2}', end='   ')
            print(f'{n} - {c:^2} = {(n-c):^2}', end='   ')
            print(f'{n} x {c:^2} = {(n*c):^2}', end='   ')
            print(f'{n} / {c:^2} = {(n/c):^2.2f}')