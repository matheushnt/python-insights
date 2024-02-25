print('COLEÇÃO DE CDS'.center(40, '='))

qtde_cds = int(input('Digite a quantidade de CDs em sua coleção: '))

total_gasto = media_gasto = c = 0
while c < qtde_cds:
    print('-' * 20)
    preco = float(input(f'Preço do {c+1}º CD: '))
    total_gasto += preco
    c += 1

media_gasto = total_gasto / c

print('INFORMAÇÕES SOBRE A COLEÇÃO'.center(40, '-'))
print(f'Valor total investido na coleção: R${total_gasto:.2f}')
print(f'Valor médio gasto: R${media_gasto:.2f}')
