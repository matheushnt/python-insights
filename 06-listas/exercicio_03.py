print('SISTEMA DE CADASTRO DE PRODUTOS'.center(45, '-'))

# Lista de produtos vazia
produtos = ['monitor', 'mouse', 'teclado', 'processador',
            'mouse pad', 'gabinete', 'air cooler', 'fams']

produto = str(input('Produto a ser cadastrado: ')).lower()

if produto not in produtos:
    produtos.append(produto)
    print(f'Produto {produto} cadastrado com sucesso!')
    print(f'Produtos cadastros:')
    print('\n'.join(produtos))
else:
    print(f'Produto já cadastrado. Insira outro produto.')
