nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Média igual a {media:.2f}. Situação: APROVADO')
elif media >= 5:
    print(f'Média igual a {media:.2f}. Situação: RECUPERAÇÃO')
else:
    print(f'Média igual a {media:.2f}. Situação: REPROVADO')
