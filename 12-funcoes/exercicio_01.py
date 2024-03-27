def analisar_bebidas(codigo: str, lista: list):
    for produto in lista:
        if codigo.upper() in produto.upper():
            print(f'Enviar produto {produto.upper()} para o setor de \
                  bebidas alcóolicas')
        elif codigo.upper() in produto.upper():
            print(f'Enviar produto {produto.upper()} para o setor de \
                  bebidas não alcóolicas')


# Programa principal
print('VERIFICADOR DE CÓDIGO DE BEBIDAS'.center(45, '='))
codigo_produtos = [
    'beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510',
    'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365', 'BEB31623',
    'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694', 'BSA11769', 'BEB19495',
    'TFA14792', 'TFA78043', 'BSA33484', 'BEB97471', 'BEB62362', 'TFA27311',
    'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947',
    'TFA58799', 'CAR94811', 'BSA59251', 'BEB15385', 'BEB24213', 'BEB56262',
    'BSA96915', 'CAR53454', 'BEB75073'
]
analisar_bebidas('BEB', codigo_produtos)
analisar_bebidas('BSA', codigo_produtos)
