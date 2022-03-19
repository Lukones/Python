temp = dict()
situação = list()
temp['Nome'] = str(input('Digite o nome do aluno: '))
temp['Media'] = float(input(f'Digite a média do {temp["Nome"]}: '))
if temp['Media'] < 6:
    temp['Situação'] = 'REPROVADO'
else:
    temp['Situação'] = 'APROVADO'
situação.append(temp.copy())
for a in situação:
    for k, v in a.items():
        print(f'{k} é igual: {v}')