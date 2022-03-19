x = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
         'Chapecoense', 'Ceará', 'Vasco',  'América-MG', 'Vitória Paraná')
print('**'*200)
print(f'Os 5 primeiros colocados do Brasileirão é {x[:6]}')
print('**'*200)
print(f'Os 4 ultimos são {x[-4:]}')
print('**'*200)
print(f'Os times em ordem alfabetica são {sorted(x)}')
print('**'*200)
print('O time da Chapecoense está na {}º posição'.format(x.index('Chapecoense')+1))
