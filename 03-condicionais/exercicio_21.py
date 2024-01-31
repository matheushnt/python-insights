print('=' * 30)
print('POSTO DE GASOLINA MATH'.center(30))
print('=' * 30)

# Preço dos combustíveis
alcool = 1.9
gasolina = 2.5

# Obtendo dados do usuário
combustivel = str(input('Informe o tipo de combustível: '))[0].upper().strip()
print('-' * 30)
litros = float(input('Litros a ser vendido: '))

# Calculando o preço e o desconto a ser pago
if combustivel == 'A':
    if litros <= 20:
        desc_alcool = 0.03
    else:
        desc_alcool = 0.05
    preco_final = litros * (alcool - (alcool * desc_alcool))
elif combustivel == 'G':
    if litros <= 20:
        desc_gasolina = 0.04
    else:
        desc_gasolina = 0.06
    preco_final = litros * (gasolina - (gasolina * desc_gasolina))
else:
    print('-' * 30)
    print('Combustível Inválido. Por favor, escolha Álcool ou Gasolina.')
    preco_final = 0    # Valor zerado para indicar erro

# Resultado
if preco_final > 0:
    print('-' * 30)
    print(f'Valor a ser pago pelo cliente: R${preco_final:.2f}')
