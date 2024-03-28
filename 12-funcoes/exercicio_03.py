def padronizar_codigos(iteravel, capitalizar='m'):
    # A função map() serve para iterar sobre os elementos do iteravel e
    # aplicar uma função
    if capitalizar == 'm':
        minusculas = list(map(lambda x: x.lower().strip(), iteravel))
        return minusculas
    elif capitalizar == 'M':
        maiusculas = list(map(lambda x: x.upper().strip(), iteravel))
        return maiusculas
    else:
        # Dispara uma Exceção de Erro de Valor
        raise ValueError('O valor deve ser apenas "m" ou "M"')


print('PADRONIZAÇÃO DE CÓDIGOS'.center(45, '-'))
codigos = (
    'AbC1234',
    'XyZ5678',
    'dEf9012',
    'GhI3456',
    'jKl7890',
    'MnO2345',
    'pQr6789'
)

print(padronizar_codigos(codigos))
