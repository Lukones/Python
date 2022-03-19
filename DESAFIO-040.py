from random import choice
from time import sleep
print('\033[4;35m*+*\033[m'*24)
print('\033[4;31mEu sou CPBOY e eu quero brincar com você de PEDRA, PAPEL ou TESOURA!!!\033[m')
print('\033[4;35m*+*\033[m'*24)
jogador = input('Por favor, digite pedra, papel ou tesoura: ').strip().capitalize()
computador = choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[33mHummmm, Quem será que ganhou?\033[m')
sleep(1)
if jogador == 'Pedra':
   if computador == 'Papel':
      print('HAAA, \033[4;32mYOU LOSEEEE!!\033[m, \033[4;34mcomo sempre a máquina ganha hahaha\033[m')
      print(f'Eu ganhei, pois, eu CPBOY escolheu \033[4m{computador}\033[m que obviamente ganha da sua \033[4m{jogador}\033[m')
   elif computador == 'Pedra':
      print(f'VISH, \033[4mempatamos eu CPBOY escolhi {computador} e você infelizmente escolheu {jogador}\033[m')
if jogador == 'Papel':
   if computador == 'Pedra':
      print('HAAA, EU GANHEI!! Uma máquina não tem a pôtencia de um cérebro')
      print(f'Eu ganhei, pois, escolhi \033[4m{jogador}\033[m que ganha da sua \033[4m{computador}\033[m CPBOY')
if jogador == 'Tesoura':
   if computador == 'Pedra':
      print('HAAA, \033[4;32mYOU LOSEEEE!!\033[m, \033[4;34mcomo sempre a máquina ganha hahaha\033[m')
      print(f'Eu ganhei, pois, eu CPBOY escolheu \033[4m{computador}\033[m que obviamente ganha da sua \033[4m{jogador}\033[m')
   elif computador == 'Tesoura':
      print(f'VISH, \033[4mEmpatamos eu CPBOY escolhi {computador} e você infelizmente escolheu {jogador}\033[m')
if jogador == 'Pedra':
   if computador == 'Tesoura':
      print('HAAA, EU GANHEI!! Uma máquina não tem a pôtencia de um cérebro')
      print(f'Eu ganhei, pois, escolhi \033[4m{jogador}\033[m que ganha da sua \033[4m{computador}\033[m CPBOY')
if jogador == 'Tesoura':
   if computador == 'Papel':
      print('HAAA, EU GANHEI!! Uma máquina não tem a pôtencia de um cérebro')
      print(f'Eu ganhei, pois, escolhi \033[4m{jogador}\033[m que ganha da seu \033[4m{computador}\033[m CPBOY')
   elif computador == 'Tesoura':
      print(f'VISH, \033[4mempatamos eu escolhi {jogador} e você CPBOY infelizmente escolheu {computador}\033[m')
if jogador == 'Papel':
   if computador == 'Tesoura':
      print('HAAA, \033[4;32mYOU LOSEEEE!!\033[m, \033[4;34mcomo sempre a máquina ganha hahaha\033[m')
      print(f'Eu ganhei, pois, eu CPBOY escolheu \033[4m{computador}\033[m que obviamente ganha da sua \033[4m{jogador}\033[m')


print(f'HUMANO: {jogador}')

print(f'MAQUINA: {computador}')
