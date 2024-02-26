from datetime import date

print('CÁLCULO DE AUMENTO SALARIAL'.center(45, '='))

ano_contratacao = int(input('Ano de Contratação: '))
salario_inicial = float(input('Salário Inicial: R$'))
print('-' * 45)

# Percentual de 1,5%
PERCENTUAL_AUMENTO = 0.015

# Importando o ano atual do Sistema Operacional
ano_atual = date.today().year
diferenca = ano_atual - ano_contratacao

# Variáveis auxiliares para os cálculos
c, soma, aumento_salarial = 1, 0, 0

while c <= diferenca:
    # O Aumento salarial corresponde ao dobro do percentual do ano anterior
    calculo_percentual = PERCENTUAL_AUMENTO * c

    # Calcula o percentual de aumento salarial
    calculo_salarial = salario_inicial * calculo_percentual

    # Soma todos os aumentos salariais
    soma += calculo_salarial
    c += 1

aumento_salarial = salario_inicial + soma

print(f'Em {ano_atual}, o salário será de R${aumento_salarial:.2f}')
