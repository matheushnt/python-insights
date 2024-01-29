""" Faça um Programa que leia três orçamentos
e mostre o maior e o menor deles """

orcamento_1 = float(input('1º Orçamento: R$'))
orcamento_2 = float(input('2º Orçamento: R$'))
orcamento_3 = float(input('3º Orçamento: R$'))
maior = menor = orcamento_1

# Verificação do maior orçamento
if orcamento_2 > orcamento_1 and orcamento_2 > orcamento_3:
    maior = orcamento_2
elif orcamento_3 > orcamento_1 and orcamento_3 > orcamento_2:
    maior = orcamento_3

# Verificação do menor orçamento
if orcamento_2 < orcamento_1:
    menor = orcamento_2
elif orcamento_3 < orcamento_1:
    menor = orcamento_3

print(f'O maior orçamento custa R${maior}. E o menor custa R${menor}')
