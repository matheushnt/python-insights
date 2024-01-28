""" Crie um novo código que calcule e dê um print no bônus dos funcionários
novamente. Porém há uma nova regra nesse 2º caso:

- A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus
 do que os outros. Então o bônus é definido da seguinte forma:

- Se vendas funcionário for maior ou igual a 20000, então o bônus é de 15%
sobre o valor de vendas
- Se vendas funcionário for menor do que 20000 e maior ou igual a 10000,
então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 10000 então
o bônus do funcionário é de 0 """

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
