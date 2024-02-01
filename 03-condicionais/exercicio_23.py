print('~' * 30)
print('AÇOUGUE MATH'.center(30))
print('~' * 30)

# Dados do usuário
tipo = str(input('Informe o tipo de carne: ')).upper().strip()
quilos = float(input('Quantidade de carne: '))
print('-' * 30)

# Estrutura para calcular o preço da carne escolhida
match tipo:
    case 'MAMINHA':
        if quilos <= 5:
            preco = 4.9 * quilos
        else:
            preco = 5.8 * quilos
    case 'ALCATRA':
        if quilos <= 5:
            preco = 5.9 * quilos
        else:
            preco = 6.8 * quilos
    case 'PICANHA':
        if quilos <= 5:
            preco = 6.9 * quilos
        else:
            preco = 7.8 * quilos

# Pedindo forma de pagamento para um possível desconto
pagamento = str(input('Forma de pagamento: '))[0].upper().strip()
print('-' * 30)

# Cálculo do preço final caso a forma de pagamento seja o cartão da loja
if pagamento in 'CM':
    DESCONTO = 0.05
    preco_final = preco - (preco * DESCONTO)
else:
    preco_final = preco

# Resultado
print(f'Valor a ser pago pelo cliente: R${preco_final:.2f}')
