sal_hora = float(input('Informe seu salário-hora: R$'))
horas_trab = int(input('Informe a quantidade de horas trabalhadas no mês: '))
sal_bruto = sal_hora * horas_trab
inss = sal_bruto * 0.1
fgts = sal_bruto * 0.11
imp_de_renda = 0
if sal_bruto <= 900:
    print('Isento(a) do Imposto de Renda')

elif sal_bruto <= 1500:
    imp_de_renda = sal_bruto * 0.05

elif sal_bruto <= 2500:
    imp_de_renda = sal_bruto * 0.1

else:
    imp_de_renda = sal_bruto * 0.2

descontos = inss + imp_de_renda
sal_liqu = sal_bruto - descontos
print('=' * 30)
print('CONTRACHEQUE'.center(30))
print('=' * 30)
print(f'Salário bruto: R${sal_bruto:.2f}')
print('-' * 30)
print(f'Imposto de Renda: R${imp_de_renda:.2f}')
print('-' * 30)
print(f'INSS: R${inss:.2f}')
print('-' * 30)
print(f'FGTS: R${fgts:.2f}')
print('-' * 30)
print(f'Total de Descontos: R${descontos:.2f}')
print('-' * 30)
print(f'Salário líquido: R${sal_liqu:.2f}')
