print(' NÍVEIS DE CO₂ NOS ESTADOS BRASILEIROS '.center(50, '='))

"""
Esses números não são indicadores reais, foram inventados somente
para fins didáticos
O exercício consiste em analisar o nível médio de CO₂ nos Estados Brasileiros
"""

# Níveis de CO₂ nos Estados Brasileiras
niveis_co2 = {
    'AC': [325, 405, 429, 486, 402],
    'AL': [492, 495, 310, 407, 388],
    'AP': [507, 503, 368, 338, 400],
    'AM': [429, 456, 352, 377, 363],
    'BA': [321, 508, 372, 490, 412],
    'CE': [424, 328, 425, 516, 480],
    'ES': [449, 506, 461, 337, 336],
    'GO': [425, 460, 385, 485, 460],
    'MA': [361, 310, 344, 425, 490],
    'MT': [358, 402, 425, 386, 379],
    'MS': [324, 357, 441, 405, 427],
    'MG': [345, 367, 391, 427, 516],
    'PA': [479, 514, 392, 493, 329],
    'PB': [418, 499, 317, 302, 476],
    'PR': [420, 508, 419, 396, 327],
    'PE': [404, 444, 495, 320, 343],
    'PI': [513, 513, 304, 377, 475],
    'RJ': [502, 481, 492, 502, 506],
    'RN': [446, 437, 519, 356, 317],
    'RS': [427, 518, 459, 317, 321],
    'RO': [517, 466, 512, 326, 458],
    'RR': [466, 495, 469, 495, 310],
    'SC': [495, 436, 382, 483, 479],
    'SP': [495, 407, 362, 389, 317],
    'SE': [508, 351, 334, 389, 418],
    'TO': [339, 490, 304, 488, 419],
    'DF': [376, 516, 320, 310, 518]
}

"""
O nível de CO₂ de um local é dado pela
média captada por 5 sensores
Para o exercício, considerei o número 450 como nível de risco 
"""
NIVEL_DE_RISCO_CO2 = 450
# Loop para iterar sobre o dicionário
for chave, valor in niveis_co2.items():
    niveis_co2_cidade = 0
    # Loop para iterar sobre a lista de níveis de CO₂
    for nivel in valor:
        niveis_co2_cidade += nivel
    media_nivel_co2_cidade = niveis_co2_cidade / 5
    if media_nivel_co2_cidade > NIVEL_DE_RISCO_CO2:
        print(f'{chave} está com níveis altíssimos de CO₂', end=' ')
        print(f'({media_nivel_co2_cidade}), é preciso chamar', end=' ')
        print('a equipe especializada para verificar a região.')
