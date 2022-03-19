from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi {min(numeros)}')
print(f'O maior valor sorteado foi {max(numeros)}')