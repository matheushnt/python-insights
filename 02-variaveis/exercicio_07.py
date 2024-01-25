""" Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês """

salario_hora = float(input('Quanto você recebe por hora?\n'))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês?\n'))
total = salario_hora * horas_trabalhadas
print(f'O salário do mês foi R${total}')
