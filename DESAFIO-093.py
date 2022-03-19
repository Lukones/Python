def contador():
    from time import sleep
    print('*' * 40)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11, 1):
        print(f'{c} ', end=' ')
        sleep(0.5)
    print('FIM! ')
    print('*' * 40)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -2, -2):
        print(f'{c} ', end=' ')
        sleep(0.5)
    print('FIM! ')
    print('*' * 40)
    print('Agora é sua vez de personalizar a contagem')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    e = int(input('Passo: '))
    print('*' * 40)
    if a > b and e > 0:
        print(f'Contagem de {a} até {b} de {e} em {e}')
        for c in range(a, (b-e), -e):
            print(f'{c} ', end=' ')
            sleep(0.5)
        print('FIM')
    if e < 0:
        print(f'Contagem de {a} até {b} de {-e} em {-e}')
        for c in range(a, (b + e), e):
            print(f'{c} ', end=' ')
            sleep(0.5)
        print('FIM')
    if e == 0 and a > b:
        print(f'Contagem de {a} até {b} de {e+1} em {e+1}')
        for c in range(a, (b - 1), -1):
            print(f'{c} ', end=' ')
            sleep(0.5)
        print('FIM')
    if e == 0 and b > a:
        print(f'Contagem de {a} até {b} de {e + 1} em {e + 1}')
        for c in range(a, (b + 1), 1):
            print(f'{c} ', end=' ')
            sleep(0.5)
        print('FIM')

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM !')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM !')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)