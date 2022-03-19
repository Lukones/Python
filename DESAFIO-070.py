tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print('=-=' * 20)
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
print('=-=' * 20)
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
print('=-=' * 20)
print('Esse são números pares informados ', end=' - ')
for n in tupla:
    if n % 2 == 0:
        print(f'{n} ', end=' - ')