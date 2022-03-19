from random import randint
from time import sleep
maior = menor = 0
jogadores = dict()
jogadores['Jogador1'] = randint(0, 6)
jogadores['Jogador2'] = randint(0, 6)
jogadores['Jogador3'] = randint(0, 6)
jogadores['Jogador4'] = randint(0, 6)
print()
print(jogadores)
print()
for k, v in jogadores.items():
    print(f'O {k} tirou : {v}')
    sleep(1)
print()
print("Ranking dos jogadores !!!")
print()
cont = 0
for item in sorted(jogadores, key = jogadores.get, reverse=True):
    cont += 1
    print (f'O {cont}º lugar vai para o: {item} com o valor do dado de {jogadores[item]}')