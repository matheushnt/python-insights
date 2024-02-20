print(' CONSUMO DE COMBUSTÍVEL '.center(40, '='))

carros = []
carro = []

DISTANCIA = 1000
PRECO_GASOLINA = 2.25

for c in range(0, 5):
    nome = str(input('Nome do carro: ')).strip().upper()
    km_litro = float(input('Km por litro: '))
    # Cálculo da quantidade de litros de combustível
    qtde_litros = DISTANCIA / km_litro
    # Cálculo do total de gasto com combustível
    total_gasto = qtde_litros * PRECO_GASOLINA
    # Inserção de dados de cada carro na lista principal 
    carro.append(nome)
    carro.append(km_litro)
    carro.append(qtde_litros)
    carro.append(total_gasto)
    carros.append(carro[:])
    carro.clear()
    print('-' * 40)

print('RELATÓRIO FINAL'. center(69, '-'))
print(f'Nº  {'CARRO':<15}{'Km/L':<10}{'TOTAL DE LITROS':>20}{'TOTAL GASTO':>20}')
print('-' * 69)
for i in range(0, len(carros)):
    print(f'{i+1}º  {carros[i][0]:<15}{carros[i][1]:<10.1f}{carros[i][2]:>20.2f}{carros[i][3]:>20.2f}')
