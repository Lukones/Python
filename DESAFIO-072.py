names = ('Casa', 'Cachorro', 'Biblioteca', 'Tenis', 'Mesa', 'Jantar', 'Mato', 'Goias')
for c in names:
    print(f'As Palavra {c} tem: ', end='')
    for x in c:
        if x in 'aeiou':
            print(x, end=' ')