from meu_pacote import string_operations
from meu_pacote.math_operations import somar, multiplicar

palavra_reversa = string_operations.string_reversa('matheus')
print(palavra_reversa)

palavra_maiuscula = string_operations.string_maiuscula('python')
print(palavra_maiuscula)

multiplicacao = multiplicar(6, 3)
print(multiplicacao)

soma = somar(6, 10)
print(soma)
