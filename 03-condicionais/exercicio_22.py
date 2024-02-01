print('=' * 30)
print('FRUTARIA MATH'.center(30))
print('=' * 30)

# Total de quilos a ser contabilizados
kg_total = 0

# Contabiliza o valor pago pelo cliente
valor_total = 0

# Calculando o preço das frutas
if (kg_morango := float(input('Informe quantos KG de morangos: '))) <= 5:
    valor_total = 2.5 * kg_morango
else:
    valor_total = 2.2 * kg_morango
print('-' * 30)
if (kg_maca := float(input('Informe quantos KG de maçã: '))) <= 5:
    valor_total += 1.8 * kg_maca
else:
    valor_total += 1.5 * kg_maca

# Quilos contabalizados
kg_total = kg_morango + kg_maca

# Calculando o desconto de 10% caso atenda a condição necessária
if kg_total > 8 or valor_total > 25:
    preco_final = valor_total - (valor_total * (10/100))

# Resultado
print('-' * 30)
print(f'Valor a ser pago pelo cliente: R${preco_final:.2f}')
