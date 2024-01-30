meta = 10000
bonus = 0
valor_funcionario = float(input('Informe o valor de vendas: R$'))
if valor_funcionario >= meta:
    bonus = valor_funcionario * (10/100)
    print(f'Bônus do funcionário: R${bonus}')
else:
    print('Não receberá bônus')
