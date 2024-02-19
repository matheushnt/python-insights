print(' DADOS METEOROLÓGICOS '.center(50, '='))

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas = [30, 29, 28, 28, 25, 26,
                20, 21, 19, 25, 27, 32]

# Cálculo da temperatura média nacional 
s = 0
for temp in temperaturas:
    s += temp
media_nacional = s / len(temperaturas)

print(f' Temperatura Média Nacional: {media_nacional:.1f}°C '.center(50, '-'))
for temp, mes in zip(temperaturas, meses):
    if temp > media_nacional:
        print(f'{mes} registrou uma temperatura média de {temp:.1f}°C')
        print('-' * 50)
