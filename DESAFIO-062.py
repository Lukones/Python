c = 0
r = 0
v = 0
x = 10
while True:
    x = int(input('Digite um número ou negativo para sair: '))
    if x > 0:
        for c in range(0, 10):
            c += 1
            r = x * c
            print(f'{x} x {c} = {r}')
    if x < 0:
        x = -1
        break
print('Acabou a Tabuada')
