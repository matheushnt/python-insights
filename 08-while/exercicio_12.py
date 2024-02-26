print(' LANCHONETE DO MATH '.center(40, '='))

lanches = ['Cachorro Quente', 'Bauru Simples',
           'Cheeseburguer', 'Refrigerante',
           'Bauru com Ovo', 'Hambúrguer']

codigos = [100, 101, 102,
           103, 104, 105]

precos = [1.2, 1.3, 1.5,
          1.2, 1.3, 1.0]

tam_lista = len(lanches)

print('CARDÁPIO'.center(40, '='))
print('{:<20}{:<10}{:<10}'.format('ESPECIFICAÇÃO', 'CÓDIGO', 'PREÇO'))
print('=' * 40)
i = 0
while i < tam_lista:
    # Tabulação do Cardápio a ser exibido
    print(f'{lanches[i]:<20}{codigos[i]:<10}R$ {precos[i]:<10}')
    print('-' * 40)
    i += 1

# Lista para armazenar todos os Pedidos do Cliente
conta = []
# Lista para armazenar cada Pedido do Cliente
pedido = []
while True:
    # Entrada do código do Pedido
    cod_pedido = int(input('Informe o código do pedido [0 para PARAR]: '))
    while cod_pedido not in [100, 101, 102, 103, 104, 105, 0]:
        cod_pedido = int(input('Informe o código do pedido [0 para PARAR]: '))

    # Caso o código seja diferente de 0, será recepcionado o Pedido do Cliente
    if cod_pedido != 0:
        # Verifica o índice do Pedido
        indice = codigos.index(cod_pedido)
        # Quantidade exigida do Pedido pelo Cliente
        qtde_pedido = int(input(f'Serão quantos {lanches[indice]}?\n'))
        # Cálculo do valor do Pedido baseado na quantidade
        valor = qtde_pedido * precos[indice]

        # Inserção do Pedido, Quantidade e o Valor Total desse Pedido
        pedido.append(lanches[indice])
        pedido.append(qtde_pedido)
        pedido.append(valor)
        conta.append(pedido.copy())
        pedido.clear()

        # Respalda o Cliente de que o Pedido foi processado
        print(f'{qtde_pedido} {lanches[indice]} PRA JÁ!!!')
        print('-' * 45)

    # Caso o código seja 0, e exibido a conta para o Cliente
    else:
        print(' - CONTA - '.center(45, '='))
        print('{:<20}{:<15}{:<10}'.format('LANCHE', 'QUANTIDADE', 'VALOR'))
        print('=' * 45)
        c = 0
        while c < len(conta):
            # Tabulação da Conta a ser exibida
            print(f'{conta[c][0]:<20}{conta[c][1]:<15}R$ {conta[c][2]:<10.2f}')
            c += 1

        # Cálculo total da Conta do Cliente
        ini = valor_total = 0
        while ini < len(conta):
            valor_total += conta[ini][2]
            ini += 1

        print('-' * 45)
        print(f'Valor total a ser pago pelo cliente: R${valor_total:.2f}')
        break
