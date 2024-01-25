""" Faça um Programa que calcule a área de uma sala de um apartamento.
Para isso, o seu programa precisa pedir a largura da sala,
 o comprimento da sala e imprimir a área em m² da sala """

comprimento = float(input('Insira o comprimento em metros (m): '))
largura = float(input('Insira a largura em metros (m): '))
area = comprimento * largura
print(f'A área da sala mede {area}m²')
