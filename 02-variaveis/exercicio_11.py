""" Faça um Programa que pergunte quanto você
 ganha por hora e o número de horas trabalhadas no mês """
salario_hora = float(input('Quanto você recebe por hora?\n'))
horas_trabalhadas = int(input('Quantas horas trabalhadas durante o mês?\n'))
print('-' * 30)

# Calcule o salário bruto
salario_bruto = salario_hora * horas_trabalhadas
print(f'Salário bruto: R${salario_bruto:.2f}')
print('-' * 30)

# Calcule o desconto do IR (11% do salário bruto)
imposto_de_renda = salario_bruto * (11/100)
print(f'Imposto de Renda: R${imposto_de_renda:.2f}')
print('-' * 30)

# Calcule o desconto do INSS (8% do salário bruto)
inss = salario_bruto * (8/100)
print(f'INSS: R${inss:.2f}')
print('-' * 30)

# Calcule o desconto do sindicato (5% do salário bruto)
sindicato = salario_bruto * (5/100)
print(f'Sindicato: R${sindicato:.2f}')
print('-' * 30)

total_de_descontos = imposto_de_renda + inss + sindicato
print(f'Total de descontos: R${total_de_descontos:.2f}')
print('-' * 30)

# Calcule o salário líquido (salário bruto - descontos)
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(f'Salário líquido: R${salario_liquido:.2f}')
