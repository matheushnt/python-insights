print(' ANÁLISE DE VENDAS '.center(45, '='))
vendas = [['Matheus', 15000],
          ['Joana', 1990],
          ['Júlia', 27000],
          ['Mario', 1030],
          ['Alon', 7870],
          ['Ana', 37500]]

meta = 10000

print('Vendedores que bateram a meta'.center(45))
print('-' * 45)
for venda in vendas:
    if venda[1] >= meta:
        print(f'{venda[0]} com {venda[1]} vendas')
        print('-' * 45)
