from datetime import date
ano = date.today().year
nascimento = int(input('Informe o ano de nascimento do atleta: '))

idade = ano - nascimento

if idade <= 9:
    print(f'O atleta possui {idade} anos, portanto sua categoria é \033[1:47mMirim\033[m.')
elif idade <= 14:
    print(f'O atleta possui {idade} anos, portanto sua categoria é \033[1:47mInfantil\033[m.')
elif idade <= 19:
    print(f'O atleta possui {idade} anos, portanto sua categoria é \033[1:47mJúnior\033[m.')
elif idade <= 20:
    print(f'O atleta possui {idade} anos, portanto sua categoria é \033[1:47mSênior\033[m.')
else:
    print(f'O atleta possui {idade} anos, portanto sua categoria é \033[1:47mMaster\033[m.')