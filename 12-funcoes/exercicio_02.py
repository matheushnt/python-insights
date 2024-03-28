def calcular_imposto(preco=0, custo=0, lucro=0):
    imposto = preco - custo - lucro
    percentual = (imposto / preco) * 100
    print(f'O Percentual do Imposto aplicado foi de {percentual:.2f}')


print(' CÁLCULO DE CARGA TRIBUTÁRIA '.center(45, '='))
calcular_imposto(2000, 500, 1000)
calcular_imposto(4560, 900, 2300)
