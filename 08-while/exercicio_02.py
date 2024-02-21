while True:
    nota = input('Informe um valor de 0 a 10: ')
    if nota.isnumeric():
        nota = int(nota)
        if 0 <= nota <= 10:
            print(f'A nota informada é igual a {nota}')
            break
    else:
        print('Nota inválida.', end=' ')
