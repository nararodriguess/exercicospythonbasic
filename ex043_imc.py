peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'\033[33mCom o IMC de {imc:.2f} você esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'\033[32mCom o IMC de {imc:.2f} você esta no seu peso ideal.')
elif 25 <= imc < 30:
    print(f'\033[33mCom o IMC de {imc:.2f} você esta com sobrepeso.')
elif 30<= imc < 40:
    print(f'\033[33mCom o IMC de {imc:.2f} você esta com obesidade.')
else:
    print(f'\033[31mCom o IMC de {imc:.2f} você está com obesidade mórbida')
