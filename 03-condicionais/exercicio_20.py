print('=' * 30)
print('INTERROGATÓRIO'.center(30))
print('=' * 30)
c = 0
perg_1 = str(input('Telefonou para a vítima?\n'))
if perg_1 in 'SIM' or perg_1 in 'sim':
    c += 1
print('-' * 30)
perg_2 = str(input('Esteve no local do crime?\n'))
if perg_2 in 'SIM' or perg_2 in 'sim':
    c += 1
print('-' * 30)
perg_3 = str(input('Mora perto da vítima?\n'))
if perg_3 in 'SIM' or perg_3 in 'sim':
    c += 1
print('-' * 30)
perg_4 = str(input('Devia para a vítima?\n'))
if perg_4 in 'SIM' or perg_4 in 'sim':
    c += 1
print('-' * 30)
perg_5 = str(input('Já Trabalhou com a vítima?\n'))
if perg_5 in 'SIM' or perg_5 in 'sim':
    c += 1
print('=' * 30)
if c == 5:
    print('Assassino')
elif c == 4 or c == 3:
    print('Cúmplice')
elif c == 2:
    print('Suspeito')
else:
    print('Continua sob investigação')
