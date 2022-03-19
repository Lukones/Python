from time import sleep
sair = False
while not sair:
    print('Por gentileza digite 2 valores.')
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    menu = True
    while menu:
        print('Carreganto...')
        sleep(1)
        print('''Obrigado, por gentileza escolha opção desejada
        [ 1 ] - Somar
        [ 2 ] - Multiplicar
        [ 3 ] - Maior
        [ 4 ] - Novos números
        [ 5 ] - Sair do programa''')
        s = int(input('Qual opção deseja: '))
        if s == 1:
            x = n1 + n2
            print('Você escolheu SOMA')
            print(f'O resultado é de: {x}')
            print('*-*'*50)
        if s == 2:
             x1 = n1 * n2
             print('Você escolheu MULTIPLICAR')
             print(f'O resultado é de: {x1}')
             print('*-*'*50)
        if s == 3:
            if n1 > n2:
                print('Você escolheu MAIOR')
                print(f'O maior número é {n1}')
                print('*-*'*50)
            elif n2 > n1:
                print('Você escolheu MAIOR')
                print(f'O maior número é {n2}')
                print('*-*'*50)
            elif n2 == n1:
                print('Você escolheu 2 nº iguais!')
                print('*-*' * 50)
        if s == 4:
            print('Você escolheu NOVOS NÚMEROS')
            menu = False
            print('*-*'*50)
        if s == 5:
            menu = False
            sair = True
            print('*-*'*50)
print('Obrigado por utilizar o programa LUKONES')


