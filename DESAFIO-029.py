# Mais um programa que da aumento para um funcionar, com uma diferença só reccebe mais se o salario for menor que x valor

sal = float(input('Digite o salário do funcionário: R$'))
if sal <= 1250.00:
    print('O salário do funcionário passará a ser de R$', sal+(sal*(15/100)))
else:
    print('O salário do funcionário passará a ser de R$', sal+(sal*(10/100)))
