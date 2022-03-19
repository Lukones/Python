dados = dict()
temp = list()
dados['nome'] = str(input('Digite o nome do jogador: '))
n = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, n):
    temp.append(int(input(f'Quantos gols na {c}º partida? ')))
    dados['gols'] = temp[:]
    dados['total'] = sum(temp)
print('-=' * 40)
print(dados)
print('-=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 40)
print(f' - O jogador {dados["nome"]} jogou {n} partidas. - ')
cont = -1
for i, v in enumerate(dados["gols"]):
    print(f'  =>   Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gol(s).')