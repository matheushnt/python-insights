""" Faça um Programa que verifique o estado civil de uma pessoa.
Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado),
"V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário
seu programa deve escrever o estado civil """

estado_civil = str(input('Estado civil (Ex: C - Casado; S - Solteiro): '))
if estado_civil == 'C':
    print('Casado')
elif estado_civil == 'S':
    print('Solteiro')
elif estado_civil == 'D':
    print('Divorciado')
elif estado_civil == 'V':
    print('Viúvo')
elif estado_civil == 'O':
    print('Outros')
