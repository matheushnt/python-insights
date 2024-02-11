print('SISTEMA DE CONSULTA DE PREÇOS'.center(45, '='))

# Produtos com seus respectivos preços
produtos = ['celular', 'câmera', 'fone de ouvido',
            'monitor', 'gabinete', 'teclado']
precos = [1850, 1100, 80, 1450, 185, 360]

produto = str(input('Produto a ser consultado o preço: ')).lower()

if produto in produtos:
    ind_produto = produtos.index(produto)
    print(f'O produto {produto} custa R${precos[ind_produto]:.2f}')
else:
    print(f'O produto {produto} não existe em nosso banco de dados')
