print('ANÁLISE DE FATURAMENTO SEMESTRAL'.center(45, '='))

maior_fat = menor_fat = media_fat = fat_total = c = 0

while c < 6:
    faturamento = float(input(f'{c+1}º Faturamento: '))
    print('- -' * 10)

    # Estrutura para analisar o maior e menor faturamento
    if c == 0:
        maior_fat = menor_fat = faturamento
    if faturamento > maior_fat:
        maior_fat = faturamento
    if faturamento < menor_fat:
        menor_fat = faturamento

    # Soma o faturamento semestral
    fat_total += faturamento

    # Calcula a média semestral
    media_fat = fat_total / 6

    c += 1

print('DASHBOARD DO FATURAMENTO SEMESTRAL'.center(45, '-'))
print(f'Maior faturamento: R${maior_fat:.2f}')
print('-' * 30)
print(f'Menor faturamento: R${menor_fat:.2f}')
print('-' * 30)
print(f'Faturamento total: R${fat_total:.2f}')
print('-' * 30)
print(f'Faturamento médio: R${media_fat:.2f}')
