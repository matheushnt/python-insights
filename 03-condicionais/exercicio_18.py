print('- -' * 10)
print('REGULAMENTO DE PESCA'.center(30))
print('- -' * 10)
quilos = float(input('Informe quantos KG de pescado: '))
print('- -' * 10)
# Limite de Quilos de Pescado: 50 Kg
if quilos > 50:
    # Cálculo do excesso de quilos
    excesso = quilos - 50
    # Cálculo da multa
    multa = 4 * excesso
    print(f'Você pescou {excesso:.2f} KG além do permitido.', end=' ')
    print(f'Deverá ser pago uma multa de R${multa:.2f}')
else:
    print(f'Você pescou {quilos:.2f} KG. Está dentro do limite,', end=' ')
    print('portanto não pagará multa.')
