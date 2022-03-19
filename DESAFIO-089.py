pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(galera)
print(galera)
print('-=' * 30)
print(f'O número de pessoas cadastrada foi de: {len(galera)}.')
print(f'A media da idade das pessoas cadastrada foi de: {media} anos.')
print('O nome das mulher(es) cadastrada(s) foi de:', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'A idade acima da média:', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
