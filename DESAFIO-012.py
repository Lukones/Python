# Um programa que resolve a hipotenusa #

from math import hypot
co = float(input('Comprimento do cateto opsoto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir: {hypot(co, ca):.2f}')

