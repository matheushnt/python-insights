""" Faça um Programa que leia o orçamento de 3 empresas
e mostre o maior deles """

maior = 0
orcamento_1 = float(input('1º Orçamento: R$'))
orcamento_2 = float(input('2º Orçamento: R$'))
orcamento_3 = float(input('3º Orçamento: R$'))
maior = orcamento_1
if orcamento_2 > orcamento_1 and orcamento_2 > orcamento_3:
    maior = orcamento_2
elif orcamento_3 > orcamento_1 and orcamento_3 > orcamento_2:
    maior = orcamento_3
print(f'O maior orçamento custa R${maior}')
