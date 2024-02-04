print('ANALISADOR DE TEXTOS'.center(40, '='))
texto1 = str(input('Primeiro texto:\n'))
print('-' * 40)
texto2 = str(input('Segundo texto:\n'))
print('-' * 40)

# Exibir os textos informados
print(f'Textos informados:\nTXT1: {texto1}\nTXT2: {texto2}')

# Tamanhos dos textos
TXT1_TAM = len(texto1)
TXT2_TAM = len(texto2)
print('-' * 40)
print(f'Quantidade de caracteres do texto 1: {TXT1_TAM}')
print(f'Quantidade de caracteres do texto 2: {TXT2_TAM}')

# Analisar se possuem o mesmo tamanho
TAM_TEXTOS = (TXT1_TAM + TXT2_TAM) / 2
if TXT1_TAM == TXT2_TAM:
    print(f'Os textos tem a mesma quantidade de caracteres: {TAM_TEXTOS:.0f}')
else:
    print('Os textos não possuem a mesma quantidade de caracteres.')

# Analisar se possuem o mesmo conteúdo ou não
TXT1_FORM = texto1.strip().replace(' ', '')
TXT2_FORM = texto2.strip().replace(' ', '')
if TXT1_FORM == TXT2_FORM:
    print('Os textos possuem o mesmo conteúdo')
else:
    print('Os textos são divergentes')
