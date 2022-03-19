lista = []
qtdn = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar [S/N]: '))
    qtdn += 1
    if s in 'Nn':
        lista.sort(reverse=True)
        print(f'Você digitou {qtdn} números na sua lista.')
        print(f'Os valores digitados foram {lista}')
        if 5 in lista:
            print(f'O valor 5 está na lista e apareceu {lista.count(5)} vez(es)')
        elif 5 not in lista:
            print('O valor 5 não se encontra na lista')
        break