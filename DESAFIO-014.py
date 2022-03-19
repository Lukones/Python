# Um programa que realiza um sorteio de um nº limitado de alunos #

from random import choice
a = input('Digite os nomes dos alunos que vão ser sorteados: ')
b = input('Digite os nomes dos alunos que vão ser sorteados: ')
c = input('Digite os nomes dos alunos que vão ser sorteados: ')
d = input('Digite os nomes dos alunos que vão ser sorteados: ')
lista = [a, b, c, d]
print(f'O aluno sorteado é: {choice(lista)}')

