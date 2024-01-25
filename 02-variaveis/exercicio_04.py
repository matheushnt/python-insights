"""Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média
de todas as notas"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média é igual a {media}')
