email = str(input('Informe o email: '))
emails_spam = 'junior@gmail.com, joao@gmail.com, nicole@gmail.com'
if email not in emails_spam:
    print('Email válido')
else:
    print('O email informado é um spam')
