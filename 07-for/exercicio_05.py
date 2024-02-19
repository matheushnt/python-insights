print(' ANÁLISE DE VENDAS '.center(30, '~'))

# Lista para armazenar os dados de todos os vendedores
vendedores = []

# Lista para armazenar os dados do vendedor a cada iteração
vendedor = []

# Soma o total de vendas para calcular a média de vendas posteriormente
s = 0
for i in range(0, 4):
    nome = str(input('Nome do Vendedor: ')).strip().capitalize()
    total_vendas = float(input('Total de Vendas: R$'))
    s += total_vendas
    vendedor.append(nome)
    vendedor.append(total_vendas)
    vendedores.append(vendedor.copy())
    vendedor.clear()
    print('-' * 30)

for info in vendedores:
    print(f'{info[0]} fez R${info[1]:.2f} em vendas')
    print('-' * 30)

media_vendas = s / 4
print(f'A média de vendas foram R${media_vendas:.2f}')
