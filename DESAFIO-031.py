# Um programa que simula análise de crédito

from time import sleep
n1 = print('Por gentileza, para aprovar seu empréstimo digite os seguintes dados: ')
n2 = float(input('Qual o valor da casa desejada? R$: '))
n3 = float(input('Qual o seu sálario mensal? R$: '))
n4 = float(input('Em quantos anos você eseja quitar a casa? '))
pres = n2/(n4*12)
desconto = (n3*(30/100))
emergencia = (n3*(35/100))
print(f'Sua parcela mensal ficará de: {pres:.2f}')
print('-=-'*20)
print('Calculando.....')
print('-=-'*20)
sleep(2)
if pres < desconto:
    print('Seu empréstimo foi \033[32maprovado, meus parábens!')
elif pres == desconto < emergencia:
    print('Seu empréstimo irá entrar em \033[1;34manálise, aguarde nosso contato\033[m')
else:
    print('Seu empréstimo foi \033[4;31mnegado\033[m')
