r1 = float(input('Digite um número: '))
r2 = float(input('Digite um número: '))
r3 = float(input('Digite um número: '))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos formam um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não formam um triângulo')
