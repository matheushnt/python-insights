from time import sleep

print(' CONSULTA DE PREÇOS '.center(30, '='))

consulta = True
while consulta:
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
        'mochila dell': 299.99
    }

    # Trecho de código para analisar se o produto está disponível ou não
    nome_produto = str(input('Nome do Produto: ')).strip().lower()
    if nome_produto in produtos.keys():
        print('Buscando preço...')
        sleep(2)
        print(f'{nome_produto.title()} custa R${produtos[nome_produto]}')
    else:
        print(f'Produto {nome_produto.title()} indisponível.')

    # Trecho de código que verifica se o Cliente quer consultar outros produtos
    sleep(2)
    resp = str(input('Nova consulta de preço [S/N]?\n'))[0].strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Nova consulta de preço [S/N]?\n'))[0].strip().upper()
    if resp == 'N':
        print('Volte Sempre!!!')
        consulta = False
