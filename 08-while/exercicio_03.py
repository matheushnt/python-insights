print(' CADASTRO DE CLIENTES '.center(30, '='))

cadastros = list()
ficha = list()

while True:
    # Entrada e validação dos dados fornecidos pelos clientes
    nome = str(input('Nome: ')).strip().capitalize()
    while not nome:
        nome = str(input('Nome: ')).strip().capitalize()
    ficha.append(nome)
    print('~' * 30)

    idade = int(input('Idade: '))
    while idade not in range(0, 151):
        idade = int(input('Idade: '))
    ficha.append(idade)
    print('~' * 30)

    salario = float(input('Salário: R$'))
    if salario <= 0:
        while salario <= 0:
            salario = float(input('Salário: R$'))
    ficha.append(salario)
    print('~' * 30)

    sexo = str(input('Sexo [M/F]: '))[0].strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: '))[0].strip().upper()
    ficha.append(sexo)
    print('~' * 30)

    print('S - Solteiro; C - Casado; V - Viúvo; D - Divorciado')
    est_civil = str(input('Estado civil [S/C/V/D]: '))[0].strip().upper()
    while est_civil not in ['S', 'C', 'V', 'D']:
        est_civil = str(input('Estado civil [S/C/V/D]: '))[0].strip().upper()
    ficha.append(est_civil)
    print('~' * 30)

    # Adição da ficha de cada cliente na lista de cadastros
    cadastros.append(ficha[:])
    ficha.clear()
    print(f'Cadastro de {nome} realizado com sucesso!')

    # Questiona se deseja cadastrar novos clientes
    resposta = str(input('Novo cadastro [S/N]?: '))[0].strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Novo cadastro [S/N]?: '))[0].strip().upper()

    # Em caso de resposta negativa, exibe todos os clientes cadastros
    if resposta == 'N':
        c = 1
        for cadastro in cadastros:
            print(f' {c}º CADASTRO '.center(30, '-'))
            print(f'Nome: {cadastro[0]}')
            print('- -' * 10)
            print(f'Idade: {cadastro[1]}')
            print('- -' * 10)
            print(f'Salário: R${cadastro[2]:.2f}')
            print('- -' * 10)
            print(f'Sexo: {cadastro[3]}')
            print('- -' * 10)
            print(f'Estado Civil: {cadastro[4]}')
            c += 1
        else:
            print(' FIM '.center(30, '='))
        break
