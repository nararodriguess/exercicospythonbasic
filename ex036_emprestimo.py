# Aprovação de empréstimos bancários

pv = float(input('Digite o valor estimado do imóvel: R$ '))
n = int(input('Digite o numero anos do financiamento: '))*12
i = float(input('Digite a taxa de juros da operação ao ano: '))/12/100
salario = float(input('Digite o salário do comprador: R$ '))
sisamrt = str(input('Digite o sistema de amortização: ')).upper().strip()

if sisamrt == 'PRICE' or sisamrt == 'SAF':
    pmt = (pv * i * ((1 + i)**n))/ (((1+i)**n) - 1)
    if pmt <= (0.3 * salario):
        print(f'Cliente possui capacidade de pagamento pois a parcela de R${pmt:.2f} não ultrapassa 30% de R${salario:.2f}')
    else:
        print(f'Infelizmente o comprador não possui capacidade de pagamento, a parcela de R${pmt:.2f} é maior que o salario de R${salario}')
elif sisamrt == 'SAC':
   pmt = (pv / n) + (i * pv)
   if pmt <= (0.3 * salario):
       print(f'Cliente possui capacidade de pagamento pois a maior parcela é de R${pmt:.2f} e não ultrapassa 30% de R${salario}')
   else:
       print(
           f'Infelizmente o comprador não possui capacidade de pagamento, parcela de R${pmt:.2f} é maior que o salario de R${salario}')
else:
    print('Erro! Digite os dados corretamente')