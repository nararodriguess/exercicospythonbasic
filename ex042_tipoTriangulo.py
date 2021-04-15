a = float(input('Digite a primeira reta do triângulo: '))
b = float(input('Digite a segunda reta do triângulo: '))
c = float(input('Digite a terceira reta do triânguo: '))

if a<= b+c and b <= a+c and c <= a+b:
    if a == b == c:
        print(f'{a}, {b} e {c} formam um triângulo Equilátero!')
    elif a == b or a==c or b==c:
        print(f'Os lados {a}, {b} e {c} formam um triângulo Isóceles!')
    else:
        print(f'Os lados {a}, {b} e {c} formam um triângulo Escaleno!')
else:
    print('Não é posssível formar um triangulo com essas retas.')