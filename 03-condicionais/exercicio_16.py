print('=' * 30)
print('BOLETIM ESCOLAR'.center(30))
print('=' * 30)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4:
    conceito = 'E'
elif media <= 6:
    conceito = 'D'
elif media <= 7.5:
    conceito = 'C'
elif media <= 9:
    conceito = 'B'
else:
    conceito = 'A'
print('-' * 30)
print(f'Média de Aproveitamento: {media:.2f}')
print(f'Conceito: {conceito}')
