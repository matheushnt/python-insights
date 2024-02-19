print('ANÁLISE DE NOTAS DE ALUNOS'.center(40, '='))

alunos = ["José", "Joana", "Maria", "Carla", "Mauricio",
          "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3]
]

# Análise das notas de cada aluno
medias = []
for lista in notas:
    # Soma as notas do aluno a cada iteração
    s = 0
    for nota in lista:
        s += nota
    media = s / 4
    medias.append(media)

# Conta quantos alunos tirou média >= 7
c = 0
for media, aluno in zip(medias, alunos):
    if media >= 7:
        c += 1
    print(f'A média de {aluno} é igual a {media:.1f}')
    print('-' * 40)

print(f'{c} alunos tiraram média maior ou igual a 7.0 pontos')
