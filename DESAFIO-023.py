# Um programa que simula um jogo de adivinhação #

from random import randint
from time import sleep

cpu = randint(0,5) # FAZ O COMPUTADOR "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente aivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # JOGADOR TENTA ADIVINHAR
print('***CALCULANDO***')
sleep(3) # PAUSA PARA DAR O RESULTADO
if jogador == cpu:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {cpu} e não no {jogador}!')
