pessoas = []
auxiliar = []
total = maispeso = menospeso = 0
while True:
    auxiliar.append(str(input('Digite o nome: ')))
    auxiliar.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maispeso = menospeso = auxiliar[1]
    else:
        if auxiliar[1] > maispeso:
            maispeso = auxiliar[1]
        if auxiliar[1] < menospeso:
            menospeso = auxiliar[1]
    pessoas.append(auxiliar[:])
    auxiliar.clear()
    rsp = str(input('Você quer continuar? [S/N] '))
    total += 1
    if rsp in 'Nn':
        break
print('-*-' * 40)
print(f'O total de pessoas: {total}')
print(f'O menor peso foi de {menospeso}Kg, que é o peso de: ', end='')
for p in pessoas:
    if p[1] == menospeso:
        print(F'[{p[0]}] ', end='')
print()
print(f'O maior peso foi de {maispeso}Kg, que é o peso de: ', end='')
for p in pessoas:
    if p[1] == maispeso:
        print(F'[{p[0]}] ', end='')


