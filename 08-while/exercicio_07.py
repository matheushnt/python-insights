print('CATEGORIZAÇÃO DE IDADES DOS COLABORADORES'.center(45, '='))

c = soma_idade = media_idade = 0
while True:
    idade = int(input('Informe sua idade: '))
    soma_idade += idade
    c += 1

    resp = str(input('Informar nova idade [S/N]?\n'))[0].strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Informar nova idade [S/N]?\n'))[0].strip().upper()

    print('-' * 45)

    if resp == 'N':
        media_idade = soma_idade / c

        print('ESTATISTICAS DA EMPRESA'.center(45, '-'))
        print(f'Média de idade dos funcionários da Empresa: {media_idade:.1f}')
        if 18 <= media_idade <= 25:
            print('A Maioria dos funcionários são Jovens')
        elif 25 <= media_idade <= 60:
            print('A maioria dos funcionários são Sêniores')
        else:
            print('A maioria dos funcionários são Pessoas Idosas')

        # Interrompe o Loop
        break
