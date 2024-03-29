def calcular_percentual(dicionario, meta):
    qtde_vendedores = len(dicionario)
    qtde_metas_batidas = 0
    vendedores = []
    for chave, valor in dicionario.items():
        if valor >= meta:
            qtde_metas_batidas += 1
            vendedores.append(chave)
    return vendedores, qtde_metas_batidas / qtde_vendedores * 100


print('PERCENTUAL DE VENDEDORES QUE BATERAM A META'.center(50, '='))
meta = 10000
vendas = {
    'Matheus': 15000,
    'Mara': 15020,
    'Samuel': 17900,
    'Maria': 3750,
    'Juliana': 10300,
    'Kayk': 7870,
    'Gislane': 18900,
    'Pedro': 9800
}
vendedores, percentual = calcular_percentual(vendas, meta)
print('funcionários bateram a meta de venda: ')
for vendedor in vendedores:
    print(vendedor)
print(f'Representando {percentual:.2f}% dos vendedores')
