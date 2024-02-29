print(' ANÁLISE DE VENDAS '.center(45, '='))

meta = 10000
vendas = [
    ('Marcos', 15000),
    ('Júlia', 27000),
    ('Ronaldo', 7890),
    ('Matheus', 11620),
    ('Maria', 9910),
    ('Ana', 24080),
    ('Tião', 10100)
]

for item in vendas:
    # Unpacking de Tupla
    nome, vendas = item

    if vendas >= meta:
        print(f'O vendedor(a) {nome} vendeu um total de R${vendas}')
        print('-' * 45)
