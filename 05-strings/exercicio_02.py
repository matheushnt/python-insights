print(' VALIDAÇÃO DE CPF '.center(40, '-'))
cpf = str(input('Informe seu CPF: ')).strip()
cpf_form = cpf.replace('.', '').replace('-', '').replace(' ', '')
if cpf_form.isnumeric() and len(cpf_form) == 11:
    print(f'Seu CPF é: {cpf_form}')
else:
    print('CPF inválido')
