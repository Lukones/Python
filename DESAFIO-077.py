num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for c, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('*'*40)
print(f'Sua lista total = {num}')
print(f'Sua lista com números impares = {impar}')
print(f'Sua lista com números pares = {par}')
