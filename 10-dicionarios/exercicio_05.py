from time import sleep

print(' REAJUSTE DE PREÇOS '.center(30, '='))

produtos = {
        'ps5': 3999.80,
        'monitor': 1230.50,
        'galaxy s24': 5399.99,
        'cadeira gamer': 1899.99,
        'teclado gamer': 459.99,
        'tablet': 2399.99,
        'iphone 14': 11999.99,
        'tv samsung': 4999.89,
        'notebook acer': 3100.50,
        'mochila dell': 299.99,
        'kindle': 359.89,
        'fone de ouvido': 289.59
}

# Loop para calcular o reajuste do preço dos produtos
for k, v in produtos.items():
    if v <= 1000:
        produtos[k] = v * 1.1
    elif 1000 <= v <= 2000:
        produtos[k] = v * 1.15
    else:
        produtos[k] = v * 1.2

consulta = True
while consulta:
    # Trecho de código para analisar se o produto está disponível ou não
    nome_produto = str(input('Nome do Produto: ')).strip().lower()
    if nome_produto in produtos.keys():
        print('Buscando preço...')
        sleep(2)
        print(f'{nome_produto.title()} custa R${produtos[nome_produto]:.2f}')
    else:
        print(f'Produto {nome_produto.title()} indisponível.')

    # Trecho de código que verifica se o Cliente quer consultar outros produtos
    sleep(2)
    resp = str(input('Nova consulta de preço [S/N]?\n'))[0].strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Nova consulta de preço [S/N]?\n'))[0].strip().upper()
    if resp == 'N':
        print('Encerrando...')
        sleep(2)
        print('Volte Sempre!!!')
        consulta = False
