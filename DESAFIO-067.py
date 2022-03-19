extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    x = int(input('Digite um valor de 0 e 20: '))
    if 0 <= x <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[x]}')




