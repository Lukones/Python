n = int(input('Vamos de tabuada? Coloque um número qualquer: '))
print(f'A tabuada do {n} segue da seguinte maneira')
for c in range(0, 11):
    r = n * c
    print(f'''{n} x {c} = \033[31m{r}\033[m''')

