# Um programa que determina se os nº digitados formam um triângulo

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um outro número: '))
n3 = float(input('Digite um outro número: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('É um TRIÂNGULO! ')
else:
    print('NÃO é um TRIÂNGULO!')
