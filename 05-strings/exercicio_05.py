
telefone = str(input('Informe seu telefone: '))

# Validar o número de telefone
numero_tel = telefone.strip().replace('-', '')
if len(numero_tel) < 8 and len(telefone) < 9:
    telefone = '3' + telefone
    numero_tel = '3' + numero_tel

# Telefone corrigido sem formatação
print(f'Telefone sem formatação: {numero_tel}')

# Telefone corrigido e com formatação
print(f'Telefone com formatação: {telefone}')
