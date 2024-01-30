print('-' * 30)
print('HORÁRIO DE ESTUDO')
print('-' * 30)
print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')
print('-' * 30)
turno = str(input('Informe o turno que você estuda [M, V, N]: '))
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido')
