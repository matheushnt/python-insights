print(' CADASTRO DE E-MAILS '.center(40, '-'))
email = str(input('Informe seu email: ')).lower().strip()
if '@' in email and '.com' in email:
    print(f'Email informado: {email}')
else:
    print('Email inválido')
