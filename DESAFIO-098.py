def ficha19(jog='<DESCONHECIIDO>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gol: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha19(gol=g)
else:
    ficha19(n, g)