total = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')

print(f'\nO número {n} foi divisível {total} vezes')
if total == 2:
    print('Isso significa que ele é um número primo!')
else:
    print('Isso significa que ele não é um número primo!')