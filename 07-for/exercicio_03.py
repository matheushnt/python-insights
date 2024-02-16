print(' INSIGHTS 2020 '.center(45, '='))
produtos = ['iphone', 'galaxy', 'ipad', 'tv',
            'máquina de café', 'kindle', 'geladeira',
            'adega','notebook dell', 'notebook hp',
            'notebook asus', 'microsoft surface',
            'webcam', 'caixa de som', 'microfone',
            'câmera canon']
vendas2019 = [558147, 712350, 573823, 405252,
              718654, 531580, 973139, 892292,
              422760, 154753, 887061, 438508,
              237467, 489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604,
              867660, 78830, 710331, 646016,
              694913, 539704, 324831, 667179,
              295633, 725316, 644622, 994303]

# Armazena os produtos mais vendidos em 2020 em comparação a 2019
insights = []

# Armazena cada produto com seu respectivo número de vendas em 2020
dados = []

# Laço para correlacionar as listas
for prod, venda2019, venda2020 in zip(produtos, vendas2019, vendas2020):
    if venda2020 > venda2019:
        # Produto e venda adicionados a lista de dados 
        dados.append(prod)
        dados.append(venda2020)
        # Lista dados adicionada a lista insights
        insights.append(dados.copy())
        # Limpeza de informações da lista dados para armazenar novos valores
        dados.clear()

print('PRODUTOS MAIS VENDIDOS EM 2020 DO QUE EM 2019')
for dado in insights:
    print(f'Produto: {dado[0]}')
    print(f'Quantidade vendida: {dado[1]}')
    print('-' * 45)
