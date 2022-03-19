from random import randint
print('*-*'*5, '\033[32mVamos Jogar?\033[m', '*-*'*5)
print('\033[31m=\033[m'*50)
print('O hoje é de advinhação, tente acerta em qual número pensei')
print('\033[31m=\033[m'*50)
h = int(input('Digite o número: '))
cpu = randint(0, 10)
tentativas = 0
while h != cpu:
    h = int(input('Errou,  tente novamente: '))
    tentativas += 1
print(f'Você venceu, eu pensei no número {cpu}, porém, tentou {tentativas} vez(es) antes de acerta')

#CORREÇÃO VAMOS ACRESCENTAR UMA PARTE PARA FICAR BEM MAIS LEGAL

computador = randint(0, 10)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que vocÊ consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Um pouco +... Tente mais uma vez")
        elif jogador > computador:
            print('Um pouco -... Tente mais uma vez')
print(f'Acertou com {palpites} tentativass. Parabéns!')