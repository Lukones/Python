jogador = dict()
time = list()
partida = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, n):
        partida.append(int(input(f'    Quantos gols na {c+1}º partida? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SsNn':
            break
        print('Erro!!! RESPONDA S OU N.')
    if resp in 'Nn':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Digite o Cod do jogador para verificar. [999 - SAIR]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(F'Erro!!! NÃO EXISSTE ESSE JOGADOR COM CÓDIGO: {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  =>   Na partida {i+1}, fez {g} gols.')
    print('*'*40)
print('<< VOLTE SEMPRE >>')