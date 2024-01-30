salario = float(input('Informe seu salário: R$'))
reajuste = 0
if salario <= 280:
    aumento = 0.2
    reajuste = salario + (salario * aumento)
    print(f'Seu salário antes do reajuste: R${salario}')
    print('O percentual de aumento aplicado: 20%')
    print(f'O valor do aumento: R$ {salario * aumento}')
    print(f'O novo salário após o reajuste: R${reajuste}')

elif salario <= 700:
    aumento = 0.15
    reajuste = salario + (salario * aumento)
    print(f'Seu salário antes do reajuste: R${salario}')
    print('O percentual de aumento aplicado: 15%')
    print(f'O valor do aumento: R$ {salario * aumento}')
    print(f'O novo salário após o reajuste: R${reajuste}')

elif salario <= 1500:
    aumento = 0.1
    reajuste = salario + (salario * aumento)
    print(f'Seu salário antes do reajuste: R${salario}')
    print('O percentual de aumento aplicado: 10%')
    print(f'O valor do aumento: R$ {salario * aumento}')
    print(f'O novo salário após o reajuste: R${reajuste}')

else:
    aumento = 0.05
    reajuste = salario + (salario * aumento)
    print(f'Seu salário antes do reajuste: R${salario}')
    print('O percentual de aumento aplicado: 5%')
    print(f'O valor do aumento: R$ {salario * aumento}')
    print(f'O novo salário após o reajuste: R${reajuste}')
