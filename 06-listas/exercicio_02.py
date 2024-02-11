from time import sleep

print(' MUDANÇA DE CARGA TRIBUTÁRIA '.center(45, '='))

# Livrarias que pagarão o imposto ao Governo
pordutos = ['Saraiva', 'Panini', 'Livraria Leitura',
            'Livraria Cultura', 'New Pop', 'Livraria Nobel']

# Cada elemento da lista corresponde a quantidade vendida no mês e o preço
vendas_preco = [[53010, 40], [25700, 35], [7500, 30],
                [5600, 45], [15105, 40], [6010, 22]]

# Preços antes do Imposto
preco_saraiva = vendas_preco[0][1]
preco_panini = vendas_preco[1][1]
preco_leitura = vendas_preco[2][1]
preco_cultura = vendas_preco[3][1]
preco_newpop = vendas_preco[4][1]
preco_nobel = vendas_preco[5][1]

# Imposto de 10% sobre o preço do livro
IMPOSTO = 0.1

# Cálculo do preço após o Imposto e Inserção do novo preço na tabela
imposto_saraiva = vendas_preco[0][1] + (vendas_preco[0][1] * IMPOSTO)
vendas_preco[0][1] = imposto_saraiva

imposto_panini = vendas_preco[1][1] + (vendas_preco[1][1] * IMPOSTO)
vendas_preco[1][1] = imposto_panini

imposto_leitura = vendas_preco[2][1] + (vendas_preco[2][1] * IMPOSTO)
vendas_preco[2][1] = imposto_leitura

imposto_cultura = vendas_preco[3][1] + (vendas_preco[3][1] * IMPOSTO)
vendas_preco[3][1] = imposto_cultura

imposto_newpop = vendas_preco[4][1] + (vendas_preco[4][1] * IMPOSTO)
vendas_preco[4][1] = imposto_newpop

imposto_nobel = vendas_preco[5][1] + (vendas_preco[5][1] * IMPOSTO)
vendas_preco[5][1] = imposto_nobel

# Impacto financeiro para cada livraria após o imposto
impacto_saraiva = (vendas_preco[0][0] * imposto_saraiva) - (vendas_preco[0][0] * preco_saraiva)
impacto_panini = (vendas_preco[1][0] * imposto_panini) - (vendas_preco[1][0] * preco_panini)
impacto_leitura = (vendas_preco[2][0] * imposto_leitura) - (vendas_preco[2][0] * preco_leitura)
impacto_cultura = (vendas_preco[3][0] * imposto_cultura) - (vendas_preco[3][0] * preco_cultura)
impacto_newpop = (vendas_preco[4][0] * imposto_newpop) - (vendas_preco[4][0] * preco_newpop)
impacto_nobel = (vendas_preco[5][0] * imposto_nobel) - (vendas_preco[5][0] * preco_nobel)

# Dados estatisticos sobre cada empresa
print(f'Livraria Saraiva:')
print(f'Preço antes do Imposto: R${preco_saraiva:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_saraiva:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_saraiva:.2f}')
print('~' * 45)
sleep(1)
print(f'Livraria Panini:')
print(f'Preço antes do Imposto: R${preco_panini:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_panini:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_panini:.2f}')
print('~' * 45)
sleep(1)
print(f'Livraria Leitura:')
print(f'Preço antes do Imposto: R${preco_leitura:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_leitura:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_leitura:.2f}')
print('~' * 45)
sleep(1)
print(f'Livraria Cultura:')
print(f'Preço antes do Imposto: R${preco_cultura:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_cultura:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_cultura:.2f}')
print('~' * 45)
sleep(1)
print(f'Livraria New Pop:')
print(f'Preço antes do Imposto: R${preco_newpop:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_newpop:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_newpop:.2f}')
print('~' * 45)
sleep(1)
print(f'Livraria Nobel:')
print(f'Preço antes do Imposto: R${preco_nobel:.2f}')
sleep(0.6)
print(f'Novo preço do livro após o Imposto: R${imposto_nobel:.2f}')
sleep(0.6)
print(f'Impacto financeiro causado após o Imposto: R${impacto_nobel:.2f}')
