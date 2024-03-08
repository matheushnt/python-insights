from time import sleep

print(' REAJUSTE DE PREÇOS '.center(100, '='))

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

reajuste_produtos = produtos.copy()

# Loop para calcular o reajuste do preço dos produtos
for k, v in produtos.items():
    if v <= 1000:
        reajuste_produtos[k] = v * 1.1
    elif 1000 <= v <= 2000:
        reajuste_produtos[k] = v * 1.15
    else:
        reajuste_produtos[k] = v * 1.2

consulta = True
while consulta:
    # Trecho de código para analisar se o produto está disponível ou não
    produto = str(input('Nome do Produto: ')).strip().lower()
    if produto in produtos.keys():
        print('Buscando preço...')
        sleep(2)
        diferenca = reajuste_produtos[produto] - produtos[produto]
        print(f'{produto.title()} custava R${produtos[produto]:.2f}. \
              Após o reajuste, custa R${reajuste_produtos[produto]:.2f}. \
                Um aumento de R${diferenca:.2f}')
        print('-' * 100)

    else:
        print(f'Produto {produto.title()} indisponível.')

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

    print('-' * 100)
