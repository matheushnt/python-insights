print('BARATÃO DO MATH'.center(35, '='))

# Preço de todos os produtos da loja
PRECO = 1.99
qtde_itens = int(input('Quantidade de itens do cliente: '))
c = total = 0

# Estrutura para calcular o valor total a ser pago pelo cliente
while c < qtde_itens:
    total += PRECO
    c += 1

print(f'Valor total a ser pago pelo cliente: R${total:.2f}')
