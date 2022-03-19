from random import choice
from random import randint
cont = 0
x = 0
while x != 'PERDER':
    regra = [('I'), ('P')]
    regra1 = randint(0, 10)
    v = int(input('Digite um valor: '))
    j = str(input('Escolha entre Impar ou Par: ')).strip().upper()[0]
    comp = choice(regra)
    compnum = regra1
    l = v + compnum
    resul = l % 2 == 0
    if resul == 0:
        if j == 'P':
            if comp == 'I':
                print('O jogador venceu')
    elif resul != 0:
        if comp == 'P':
            if j == 'I':
                print('O jogador venceu')
    elif resul != 0:
        if j == 'P':
            if comp == 'I':
                print('O computador venceu')
                x = 'PERDER'
                print(f'Você escolheu {j} e o PC ecolheu {comp}')
                print(f'Você escolheu: {v}, O pc escolheu: {regra1}, Somando os dois da: {l}, E a soma resulta em um número: {resul}.')
                break
    elif resul == 0:
        if comp == 'P':
            if j == 'I':
                print('O computador venceu')
                x = 'PERDER'
                print(f'Você escolheu {j} e o PC ecolheu {comp}')
                print(f'Você escolheu: {v}, O pc escolheu: {regra1}, Somando os dois da: {l}, E a soma resulta em um número: {resul}.')
                break
    print(f'Você escolheu {j} e o PC ecolheu {comp}')
    print(f'Você escolheu: {v}, O pc escolheu: {regra1}, Somando os dois da: {l}, E a soma resulta em um número: {resul}.')
    cont += 1
print(f'O jogador venceu {cont} vezes antes de perder')