print(' QUEM FOI O MELHOR JOGADOR? '.center(45, '='))

jogadores = ['João', 'Pedro', 'Lucas', 'Marcos', 'André',
             'Ronaldo', 'Gabriel', 'Matheus', 'Rafael',
             'Gustavo']

# Contadores de voto para cada jogador
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0

# Lista para armazenar a quantidade de votos de cada jogador
votos = []

# Loop Principal
while True:
    # Entrada e validação dos votos
    voto = int(input('Digite o número do Jogador [999 para PARAR]: '))
    if voto != 999:
        while voto not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print('Jogador inexistente. Por favor, ', end='')
            voto = int(input('Digite o número do Jogador [999 para PARAR]: '))

        jogador = jogadores[voto-1]
        print(f'Jogador {jogador} recebeu um voto!')
        print('- -' * 15)

        # Estrutura para quantificar os votos de cada jogador
        if voto != 0:
            match voto:
                case 1:
                    c1 += 1
                case 2:
                    c2 += 1
                case 3:
                    c3 += 1
                case 4:
                    c4 += 1
                case 5:
                    c5 += 1
                case 6:
                    c6 += 1
                case 7:
                    c7 += 1
                case 8:
                    c8 += 1
                case 9:
                    c9 += 1
                case 10:
                    c10 += 1
    else:
        # Inserção dos votos de cada jogador na Lista Votos
        votos.append(c1)
        votos.append(c2)
        votos.append(c3)
        votos.append(c4)
        votos.append(c5)
        votos.append(c6)
        votos.append(c7)
        votos.append(c8)
        votos.append(c9)
        votos.append(c10)

        # Loop para contabilizar o total de votos
        qtde_votos, tam_lista_votos = 0, len(votos)
        for i in range(0, tam_lista_votos):
            qtde_votos += votos[i]

        # Loop para calcular o percentual de cada jogador
        # E verificar o jogador mais votado
        c, percentual_jogadores = 0,  []
        votos_melhor_jogador, melhor_jogador = 0, ''
        while c < tam_lista_votos:
            percentual = votos[c] / qtde_votos
            percentual_jogadores.append(percentual)

            # Analisar o mais votado
            if c == 0 or votos[c] > votos_melhor_jogador:
                votos_melhor_jogador = votos[c]
                melhor_jogador = jogadores[c]
            c += 1

        # Cabeçalho da apresentação dos resultados
        print('RESULTADO DA VOTAÇÃO'.center(45, '='))
        print(f'Foram computados {qtde_votos} votos')
        print('=' * 45)
        print('{:<15}{:>8}{:>15}'.format('JOGADOR', 'VOTOS', 'PERCENTUAL'))
        print('=' * 45)

        # Loop para exibirr o resultado da votação de forma tabulada
        ini, pj = 0, percentual_jogadores
        while ini < len(jogadores):
            print(f'{jogadores[ini]:<15}{votos[ini]:>8}{pj[ini]:>15.1%}')
            print('-' * 45)
            ini += 1

        # Exibição do jogador mais votado
        print(f'O jogador mais votado é o {melhor_jogador}')
        print(f'Com {votos_melhor_jogador} votos')

        # Interrompe o Loop Principal
        break
