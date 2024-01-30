produto_1 = float(input('Preço do 1º produto: R$'))
produto_2 = float(input('Preço do 2º produto: R$'))
produto_3 = float(input('Preço do 3º produto: R$'))
menor = produto_1
if produto_2 < produto_1 and produto_2 < produto_3:
    menor = produto_2
elif produto_3 < produto_1 and produto_3 < produto_2:
    menor = produto_3
print(f'O produto com menor preço custa R${menor}')
