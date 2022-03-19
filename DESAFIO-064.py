from time import sleep
cont18 = conthomen = contF20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
    print('='*30)
    print('\033[4;31mCADASTRANDO...\033[m')
    print('='*30)
    sleep(1)
    if sexo in 'Ff':
        if idade <= 20:
            contF20 += 1
    if sexo in 'Mm':
        conthomen += 1
    if idade >= 18:
        cont18 += 1
    dnv = ' '
    while dnv not in 'SsNn':
        dnv = str(input('Deseja continuar a cadastrar pessoas? [S/N] ')).strip().upper()[0]
    if dnv in 'Nn':
        break
print(f'Você cadastrou um total de {cont18} pessoa(s) acima de 18 anos')
print(f'Você cadastrou um total de {conthomen} homens')
print(f'Você cadastrou um total de {contF20} mulheres com menos de 20 anos')

