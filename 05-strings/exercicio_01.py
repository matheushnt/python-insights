print(' CADASTRO DE CPF '.center(45, '-'))
cpf = str(input('Informe seu CPF (Insira apenas números): '))
print('-' * 30)
if len(cpf) == 11 and cpf.isnumeric():
    print(f'Seu CPF é: {cpf}')
else:
    print('CPF inválido')
