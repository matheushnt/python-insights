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

# Preço total até o momento, podendo receber desconto
preco_total = preco

# Pedindo forma de pagamento para um possível desconto
pagamento = str(input('Forma de pagamento: '))[0].upper().strip()

# Verificar a possibilidade de desconto de 5%
aprov = False

# Cálculo do preço final caso a forma de pagamento seja o cartão da loja
if pagamento in 'CM':
    # Desconto aprovado
    aprov = True
    DESCONTO = 0.05
    preco_final = preco_total - (preco_total * DESCONTO)
else:
    preco_final = preco_total

# Resultado
print('~' * 30)
print('{:^30}'.format('CUPOM FISCAL'))
print('-' * 30)
print(f'Tipo de carne: {tipo}')
print('-' * 30)
print(f'Quantidade pedida de {tipo}: {quilos:.2f} KG')
print('-' * 30)
print(f'Preço total: R${preco_total:.2f}')
print('-' * 30)
if aprov:
    print('Desconto: 5%')
else:
    print('Desconto: NENHUM DESCONTO APLICADO')
print('-' * 30)
print(f'Preço final: R${preco_final:.2f}')
