var = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while var not in 'MF':
    print('Digite os dados corretamente!')
    var = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
print('Dados registrados!')