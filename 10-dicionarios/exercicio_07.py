print('ANÁLISE DE PERCENTUAL DE AUMENTO'.center(45, '='))

semestre_1_2022 = {
    'jan': 15000,
    'fev': 15500,
    'mar': 14000,
    'abr': 16600,
    'mai': 16300,
    'jun': 17000
}

semestre_1_2023 = {
    'jan': 17000,
    'fev': 15000,
    'mar': 17500,
    'abr': 16900,
    'mai': 16000,
    'jun': 18500
}

# Criando uma lista de tuplas, cada tupla é o número de vendas de 2022 e 2023
vendas = list(zip(semestre_1_2022.values(), semestre_1_2023.values()))
# Criando o dicionário com os meses e suas vendas nos anos de 2022 e 2023
meses_percentuais = dict(zip(semestre_1_2022.keys(), vendas))
# Variável auxiliar para calcular o crescimento total entre os anos
percentual_total = 0

for mes, vendas in meses_percentuais.items():
    # Unpacking de Tupla
    vendas_2022, vendas_2023 = vendas
    if vendas_2023 > vendas_2022:
        percentual = (vendas_2023 / vendas_2022) - 1
        percentual_total += percentual
        print(f'{mes.upper()} teve um aumento de {percentual:.1%}')
        print('-' * 30)

print(f'O percentual total de crescimento foi {percentual_total:.1%}')
