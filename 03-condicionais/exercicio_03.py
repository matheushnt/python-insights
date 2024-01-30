estoque_min_alimentos = 70
estoque_min_bebidas = 50
estoque_min_limpeza = 30

categoria = input('Informe a categoria do Produto: ')
print('-' * 30)
produto = input('Informe o nome do Produto: ')
print('-' * 30)
quantidade = input('Informe a quantidade em estoque do Produto: ')
print('-' * 30)
if categoria and produto and quantidade:
    quantidade = int(quantidade)
    if categoria == 'alimentos' and quantidade < estoque_min_alimentos:
        print(f'Solicitar {produto} à equipe de compras')
        print(f'Temos apenas {quantidade} unidades em estoque')

    elif categoria == 'bebidas' and quantidade < estoque_min_bebidas:
        print(f'Solicitar {produto} à equipe de compras')
        print(f'Temos apenas {quantidade} unidades em estoque')

    elif categoria == 'limpeza' and quantidade < estoque_min_limpeza:
        print(f'Solicitar {produto} à equipe de compras')
        print(f'Temos apenas {quantidade} unidades em estoque')
else:
    print('Preencha os dados corretamente')
