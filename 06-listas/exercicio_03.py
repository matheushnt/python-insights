print('SISTEMA DE CADASTRO DE PRODUTOS'.center(45, '-'))

# Lista de produtos vazia
produtos = list()

produto = str(input('Produto a ser cadastrado: ')).lower()

if produto not in produtos:
    produtos.append(produto)
    print(f'Produto {produto} cadastrado com sucesso!')
    print(f'Produtos cadastros: {produtos}')
else:
    print(f'Produto já cadastrado. Insira outro produto.')
