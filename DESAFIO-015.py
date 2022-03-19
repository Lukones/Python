# Um programa que realiza um sorteio de pessoas e determina a ordem #

from random import shuffle
a = input('Digite os nomes dos alunos que vão ser sorteados: ')
b = input('Digite os nomes dos alunos que vão ser sorteados: ')
c = input('Digite os nomes dos alunos que vão ser sorteados: ')
d = input('Digite os nomes dos alunos que vão ser sorteados: ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)