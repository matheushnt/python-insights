print('=' * 30)
print('BANCO MATH'.center(30))
print('=' * 30)
diferenca = n100 = n50 = n10 = n5 = n1 = 0
# Uso do Walrus Operator. Utilizado quando pretende-se usar e atribuir um valor
# a uma variável com uma linha de código
if 10 <= (dinheiro := int(input('Valor a ser sacado: R$'))) <= 600:
    # Notas de 100 reais
    if dinheiro >= 100:
        n100 = dinheiro // 100
        diferenca = dinheiro % 100
    # Notas de 50 reais
    if diferenca >= 50 or dinheiro >= 50:
        n50 = diferenca // 50
        diferenca %= 50
    # Notas de 10 reais
    if diferenca >= 10 or dinheiro >= 10:
        n10 = diferenca // 10
        diferenca %= 10
    # Notas de 5 reais
    if diferenca >= 5 or dinheiro >= 5:
        n5 = diferenca // 5
        diferenca %= 5
    # Moedas de 1 real
    if diferenca >= 1 or dinheiro >= 1:
        n1 = diferenca // 1
        diferenca %= 1

    print('=' * 30)
    print('Foram sacadas:')
    if n100 > 0:
        print(f'{n100} nota(s) de 100 reais')
    if n50 > 0:
        print('-' * 30)
        print(f'{n50} nota(s) de 50 reais')
    if n10 > 0:
        print('-' * 30)
        print(f'{n10} nota(s) de 10 reais')
    if n5 > 0:
        print('-' * 30)
        print(f'{n5} nota(s) de 5 reais')
    if n1 > 0:
        print('-' * 30)
        print(f'{n1} moeda(s) de 1 real')
    print('=' * 30)
    print('Volte sempre ao Banco Math!')

else:
    print('=' * 30)
    print(f'Não é possível sacar R${dinheiro}')
    print('Valor mínimo é de R$10 e o máximo é R$600')
