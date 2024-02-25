print('ELEIÇÕES 2026'.center(45, '='))

CANDIDATO_1 = 'MATHEUS'
CANDIDATO_2 = 'SAMUEL'
CANDIDATO_3 = 'KAYK'

c1 = c2 = c3 = 0
print('10 para MATHEUS  --  25 para SAMUEL  --  30 para KAYK')
while True:
    # Candidato a ser votado
    voto = int(input('Informe o número do candidato: '))
    while voto not in [10, 25, 30]:
        print('Candidato não encontrado. ', end='')
        voto = int(input('Informe o número do candidato: '))

    # Estrutura para contabilizar os votos de cada candidato
    match voto:
        case 10:
            c1 += 1
        case 25:
            c2 += 1
        case 30:
            c3 += 1

    # Questiona se ainda haverá mais votos
    resp = str(input('Novo voto [S/N]?\n'))[0].strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Novo voto [S/N]?\n'))[0].strip().upper()
    print('-' * 45)

    # Em caso negativo ao questionamento, exibe as estatisticas das eleições
    if resp == 'N':
        print('ESTATISTICAS DAS ELEIÇÕES DE 2026'.center(45, '-'))
        print(f'O Candidato {CANDIDATO_1} recebeu {c1} votos')
        print('-' * 45)
        print(f'O Candidato {CANDIDATO_2} recebeu {c2} votos')
        print('-' * 45)
        print(f'O Candidato {CANDIDATO_3} recebeu {c3} votos')
        print('-' * 45)

        votos = [c1, c2, c3]
        mais_votado = max(votos)
        if c1 == mais_votado:
            print(f'O Candidato {CANDIDATO_1} é o VENCEDOR!!!'.center(45, '='))
        elif c2 == mais_votado:
            print(f'O Candidato {CANDIDATO_2} é o VENCEDOR!!!'.center(45, '='))
        else:
            print(f'O Candidato {CANDIDATO_3} é o VENCEDOR!!!'.center(45, '='))

        # Interrompe o Loop
        break
