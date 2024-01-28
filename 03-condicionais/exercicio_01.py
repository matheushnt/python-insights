""" Crie um programa que calcule e dê um print no bônus que os
funcionários devem receber segundo a regra:

- A meta é R$20000 em vendas
- Se o valor de vendas for maior ou igual a meta, o valor do bônus do
funcionário é 10% do valor de vendas
- Caso contrário o valor de bônus do funcionário é 0
Print o bônus dos 3 funcionários """

meta = 10000
bonus = 0
valor_funcionario = float(input('Informe o valor de vendas: R$'))
if valor_funcionario >= meta:
    bonus = valor_funcionario * (10/100)
    print(f'Bônus do funcionário: R${bonus}')
else:
    print('Não receberá bônus')
