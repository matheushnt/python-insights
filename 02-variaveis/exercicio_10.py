""" Tendo como dados de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula """

altura = float(input('Informe sua altura: '))
peso_ideal_homem = 72.7 * altura - 58
peso_ideal_mulher = 62.1 * altura - 44.7
print(f'O peso ideal com essa altura para homens é {peso_ideal_homem} Kg')
print(f'O peso ideal com essa altura para mulheres é {peso_ideal_mulher} Kg')
