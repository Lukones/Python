from random import randint
from time import sleep
numeros = list()


def sorteia():
    print(f'Os 5º sorteados foram: ', end='')
    for c in range(1, 6):
        a = randint(0, 10)
        print(f'{a} ', end='')
        sleep(0.2)
        if c >= 0:
            numeros.append(a)


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'\nOs valores sorteados {numeros} que são par tem a soma total de {soma}')


sorteia()
somaPar()
