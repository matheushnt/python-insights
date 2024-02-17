print(' ANÁLISE DE VENDAS '.center(40, '='))

# Armazena as informações de todos os vendedores
vendas = []

# Lista auxiliar que armazena as informações de cada vendedor
ficha = []

for c in range(0, 5):
    vendedor = str(input('Nome do vendedor: ')).strip().capitalize()
    venda = int(input('Total de vendas: R$'))
    ficha.append(vendedor)
    ficha.append(venda)
    vendas.append(ficha[:])
    ficha.clear()
    print('~' * 30)

meta = 10000

# Armazena os nomes dos vendedores que bateram a meta
lista_vendedores = list()

for item in vendas:
    # Analisa se as vendas do vendedor é igual ou superior a meta
    if item[1] >= meta:
        # Adiciona o nome do vendedor na lista de vendedores que bateram a meta
        lista_vendedores.append(item[0])

# Percentual de vendedores que bateram a meta
percentual = len(lista_vendedores) / len(vendas)

print(' VENDEDORES QUE BATERAM A META '.center(40, '='))
for vendedor in lista_vendedores:
    print(vendedor)
    print('-' * 40)

print(f'Percentual de vendedores que bateram a meta: {percentual:.1%}')
