print('-' * 30)
print('ANO BISSEXTO'.center(30))
print('-' * 30)
ano = int(input('Informe um ano: '))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} não é Bissexto')
