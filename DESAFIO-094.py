from time import sleep
def maior(* núm):
    cont = maior = 0
    print('*' * 40)
    print('Analisando os valores passados...')
    for c in núm:
        print(f'{c} ', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo.', end=' ')
    print()
    print(f'O maior nª informado foi: {maior}')



maior(0, 4, 8, 5, 6, 7)
maior(4, 7, 0)
maior(1, 2)
maior()