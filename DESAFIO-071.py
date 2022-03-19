tuplas = ('Caderno', 22, 'Lápis', 1, 'Caneta', 13, 'Estojo', 15, 'Apostila', 20)
print('*'*40)
print(f'{"LSITA DE ITENS":^40}')
print('*'*40)
for pos in range(0, len(tuplas)):
    if pos % 2 == 0:
        print(f'{tuplas[pos]:.<30}', end='')
    else:
        print(f'R${tuplas[pos]:>7.2f}')
print('*' * 40)