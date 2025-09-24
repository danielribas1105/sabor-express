valor_conta = float(input('Digite o valor da conta: '))
porcentagem = float(input('Digite a porcentagem da gorjeta: '))

gorjeta = valor_conta * (porcentagem/100)
print(f'Valor da gorjeta: R${gorjeta:.2f}')
print(f'Total a pagar: R${(valor_conta + gorjeta):.2f}')