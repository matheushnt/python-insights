""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
 em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
 é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
 latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
 de latas de tinta a serem compradas e o preço total """

area = float(input('Informe a área (m²) a ser pintada: '))
print('=' * 30)

# Quantos litros necessários para pintar toda a área
litros_tinta = area / 3

# Quantidade de latas necessárias
latas = litros_tinta / 18

# Preço gasto com todas as latas
preco_total = latas * 80

print(f'Quantidade de latas necessárias: {latas:.2f}')
print('=' * 30)
print(f'Preço total gasto na compra das latas: {preco_total}')
