nascimento = int(input('Digite o ano do seu nascimento: '))

from datetime import date
idade = (date.today().year) - nascimento

if idade < 18:
    anos = 18 - idade
    print(f'Você ainda deve se alistar no serviço militar. Faltam {anos} anos para você se alistar.')
elif idade == 18:
    print('Caso não tenha se alistado, você deve se alistar nesse ano.')
else:
    anos = idade - 18
    print(f'Você já deve ter se alistado, caso não tenha se alistado, passou {anos} anos do prazo de alistamento.')

