""" Vamos criar um conversor de temperatura. Faça um Programa que peça
a temperatura em graus Fahrenheit, transforme e mostre a temperatura
em graus Celsius """

fahrenheit = float(input('Informe a temperatura em graus Fahrenheit (°F): '))
celsius = (fahrenheit - 32) / 1.8
print(f'{fahrenheit}°F é igual a {celsius}°C')
