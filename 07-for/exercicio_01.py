from time import sleep

print(' REGISTRO DE HÓSPEDES '.center(45, '='))

# Lista para armazenar as informações de todos os hóspedes
quarto = []

qtde_pessoas = int(input('Quantidade de hóspedes no quarto: '))

# Laço para cadastrar os hóspedes no quarto
for c in range(qtde_pessoas):
    # Lista para armazenar as informações de cada hóspede
    ficha = []
    nome = str(input(f'Nome do {c+1}º Hóspede: ')).capitalize()
    ficha.append(nome)
    cpf = str(input(f'CPF do {c+1}º Hóspede: ')).replace('.', '').replace('-', '')
    ficha.append(cpf)
    quarto.append(ficha[:])
    ficha.clear()
    print('-' * 45)

print(' INFORMAÇÕES SOBRE HÓSPEDES '.center(45, '-'))

# Variável para indexar cada hóspede durante a iteração do laço
c = 1

# Laço para exibir as informações sobre cada hóspede
for pessoa in quarto:
    print(f'{c}º Hóspede:')
    print(f'Nome: {pessoa[0]}')
    print(f'CPF: {pessoa[1]}')
    print('-' * 45)
    c += 1
    sleep(0.5)
