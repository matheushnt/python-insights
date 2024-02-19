print(f' ORGANIZAÇÕES MATH '.center(30, '='))

# Lista para armazenar os salários dos colaboradores
salarios = []

for c in range(1, 6):
    salario = float(input(f'{c}º Salário: R$'))
    salarios.append(salario)
    print('-' * 30)

QTDE_FUNCIONARIOS = len(salarios)

PERCENTUAL_ABONO = 0.2

# Lista para armazenar os abonos dos colaboradores
abonos = []
abono_min = total_abono = maior_abono = 0

for salario in salarios:
    # Cáculo do abono
    abono = salario * PERCENTUAL_ABONO
    # Soma o total gasto com os abonos
    total_abono += abono
    # Conta quantos valores mínimos de abono serão pagos
    if abono == 100:
        abono_min += 1
    # Adiciona o abono na lista de abonos
    abonos.append(abono)
    # Estrutura para analisar o maior valor pago de abono
    if  abono == abonos[0]:
        maior_abono = abono
    elif abono > maior_abono:
        maior_abono = abono

# Exibição do resultado
print('ESTATISTICAS'.center(30, '-'))
print(f'{'SALÁRIO':<15}{'ABONO':>15}')
print('-' * 30)

for i in range(0, len(salarios)):
    print(f'{salarios[i]:<15.2f}{abonos[i]:>15.2f}')
    print('- -' * 10)

print(f'Quantidade de funcionários: {QTDE_FUNCIONARIOS}')
print(f'Total gasto com abonos: R${total_abono:.2f}')
print(f'Valor mínimo pago a {abono_min} colaborador(es)')
print(f'Maior valor de abono pago: R${maior_abono}')
