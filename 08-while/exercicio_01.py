print(' REGISTRO DE VENDAS '.center(45, '='))

vendas = []
registro = []

while True:
    # Entrada de dados
    produto = str(input('Digite o produto: ')).strip().upper()
    qtde_vendida = int(input('Quantidade vendida: '))
    # Registro nas listas
    registro.append(produto)
    registro.append(qtde_vendida)
    vendas.append(registro.copy())
    # Limpa de dados após o registro finalizar
    registro.clear()
    # Retorno ao usuário que o registro foi finalizado
    print(f'Produto {produto} registrado com sucesso!')
    print('-' * 45)

    # Verificação se o usuário quer fazer novos registros
    resp = str(input('Fazer novo registro [S/N]?\n'))[0].upper().strip()
    if resp == 'S':
        pass
    elif resp != 'N':
        resp = str(input('Fazer novo registro [S/N]?\n'))[0].upper().strip()
    if resp == 'N':
        print('PRODUTOS REGISTRADOS'.center(45, '-'))
        for i in range(0, len(vendas)):
            print(f'Produto: {vendas[i][0]}')
            print(f'Quantidade de vendas: {vendas[i][1]}')
            print('-' * 45)
        break
