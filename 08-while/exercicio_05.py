print('ANÁLISE DA POPULAÇÃO'.center(30, '='))

pais_a = int(input('População do Pais A: '))
taxa_crescimento_pais_a = float(input('Taxa de Crescimento do País A: '))
percentual_pais_a = pais_a * (taxa_crescimento_pais_a / 100)

pais_b = int(input('População do País B: '))
taxa_crescimento_pais_b = float(input('Taxa de Crescimento do País B: '))
percentual_pais_b = pais_b * (taxa_crescimento_pais_b / 100)

aumento_populacao_pais_a = aumento_populacao_pais_b = anos = 0
while True:
    aumento_populacao_pais_a = percentual_pais_a
    pais_a += aumento_populacao_pais_a

    aumento_populacao_pais_b = percentual_pais_b
    pais_b += aumento_populacao_pais_b

    if pais_a > pais_b:
        print(f'Em {anos} anos o País A chegará a marca de ', end='')
        print(f'{pais_a} habitantes. Ou seja, ', end='')
        print('ultrapassando o País B.')
        print(pais_b)
        break

    anos += 1
