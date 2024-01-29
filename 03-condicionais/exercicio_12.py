""" Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso """

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
