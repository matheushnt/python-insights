print(' FATURAMENTO DE 2023 '.center(45, '='))
# Dados importantes sobre o faturamento anual
meses = ['janeiro', 'fevereiro', 'março', 'abril',
         'maio', 'junho', 'julho', 'agosto',
         'setdmbro', 'outubro', 'novembro', 'dezembro']
vendas_1sem = [25000, 29000, 22200,
               17750, 15870, 19900,]
vendas_2sem = [19850, 20120, 17500,
               16920, 49400, 9845]
vendas_anual = vendas_1sem + vendas_2sem

# Definindo métricas
melhor_mes = max(vendas_anual)
ind_melhor = vendas_anual.index(melhor_mes)
pior_mes = min(vendas_anual)
ind_pior = vendas_anual.index(pior_mes)
fat_total = sum(vendas_anual)
percentual_melhor = melhor_mes / fat_total

# Definindo o Top 3
top3 = []

# Cópia da lista vendas_anual
vendas_total = vendas_anual[:]

# Selecionando o 1º maior faturamento
fat_maior = max(vendas_total)
top3.append(fat_maior)
vendas_total.remove(fat_maior)

# Selecionando o 2º maior faturamento
fat_maior = max(vendas_total)
top3.append(fat_maior)
vendas_total.remove(fat_maior)

# Selecionando o 3º maior faturamento
fat_maior = max(vendas_total)
top3.append(fat_maior)
vendas_total.remove(fat_maior)

# Dados estatisticos
print(f'O faturamento total de 2023 foi de R${fat_total}')
print('-' * 45)
print(f'Melhor mês: {meses[ind_melhor]} com R${melhor_mes} de faturamento')
print('-' * 45)
print(f'Pior mês: {meses[ind_pior]} com R${pior_mes} de faturamento')
print('-' * 45)
print(f'O melhor mês representou {percentual_melhor:.1%} do total de vendas')
print('-' * 45)
print(f'Top 3 maiores faturamentos: {top3}')
