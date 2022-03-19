n = int(input('Digite o primeiro valor: '))
n1 = int(input('Digite o segundo valor: '))
if n > n1:
    print(f'O valor {n} é maior do que o segundo.')
elif n1 > n:
    print(f'O valor {n1} é maior que o primeiro.')
else:
    print('Não existe valor maior, os dois são iguais')