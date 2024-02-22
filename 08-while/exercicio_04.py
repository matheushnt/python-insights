print('ANÁLISE DA POPULAÇÃO'.center(30, '='))

PAIS_A = 80000
TAXA_CRESCIMENTO_PAIS_A = 0.03
PERCENTUAL_PAIS_A = PAIS_A * TAXA_CRESCIMENTO_PAIS_A

PAIS_B = 200000
TAXA_CRESCIMENTO_PAIS_B = 0.015
PERCENTUAL_PAIS_B = PAIS_B * TAXA_CRESCIMENTO_PAIS_B

aumento_populacao_pais_a = anos = 0
while aumento_populacao_pais_a < PAIS_B:
    aumento_populacao_pais_a += PERCENTUAL_PAIS_A
    anos += 1

if aumento_populacao_pais_a >= PAIS_B:
    print(f'É necessário {anos} anos para o País A chegar a marca de ', end='')
    print(f'{aumento_populacao_pais_a} habitantes. Consequentemente, ', end='')
    print('ultrapassando o País B.')
