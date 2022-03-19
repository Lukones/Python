from math import factorial
n = 0
while n != 'N':
  n = int(input('Digite um valor para saber seu fatorial: '))
  fac = factorial(n)
  print(f'O valor fatorial do {n} é {fac}')
  n = str(input('Deseja saber outro? Digite [S/N]: ')).strip().upper()
print('Muito Obrigado por usar nosso programa')

#CORREÇÃO - EU UTILIZEI UM FUNÇÃO JÁ NO SISTEMA KKKK VAMOS VER COMO FAZER  MANUAL

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
  print('{}'.format(c), end=' ')
  print(' x ' if c > 1 else ' = ', end=' ')
  f *= c
  c -= 1
print('{}'.format(f))

