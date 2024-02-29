print(' ANÁLISE DO PERCENTUAL DE AUMENTO DE VENDAS '.center(90, '='))

vendas_produtos = [
        ('iphone', 558147, 951642),
        ('galaxy', 712350, 244295),
        ('ipad', 573823, 26964),
        ('tv', 405252, 787604),
        ('máquina de café', 718654, 867660),
        ('kindle', 531580, 78830),
        ('geladeira', 973139, 710331),
        ('adega', 892292, 646016),
        ('notebook dell', 422760, 694913),
        ('notebook hp', 154753, 539704),
        ('notebook asus', 887061, 324831),
        ('microsoft surface', 438508, 667179),
        ('webcam', 237467, 295633),
        ('caixa de som', 489705, 725316),
        ('microfone', 328311, 644622),
        ('câmera canon', 591120, 994303)
]

for item in vendas_produtos:
    # Unpacking de Tupla
    produto, vendas2019, vendas2020 = item

    if vendas2020 > vendas2019:
        # Cálculo do percentual de aumento
        percentual_aumento = (vendas2020 / vendas2019) - 1

        # Exibição dos resultados
        print('{} teve {} vendas em 2019 e {} vendas em 2020.'
              .format(produto, vendas2019, vendas2020), end=' ')
        print(f'Crescimento de {percentual_aumento:.2%}')
        print('-' * 90)
