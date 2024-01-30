meta = 10000
bonus = 0
vendas_funcionario = float(input('Valor de vendas: R$'))
if vendas_funcionario >= 20000:
    bonus = vendas_funcionario * 0.15
    print(f'Bônus de 20% para o funcionário: R${bonus}')

elif 10000 <= vendas_funcionario < 20000:
    bonus = vendas_funcionario * 0.1
    print(f'Bônus de 10% para o funcionário: R${bonus}')

else:
    print('Funcionário não recebe bônus')
