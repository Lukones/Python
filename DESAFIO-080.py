temp = [[], []]
for c in range(0,7):
    n = (int(input(f'Digite o {c+1}º valor: ')))
    if n % 2 == 0:
        temp[0].append(n)
        temp[0].sort()
    else:
        temp[1].append(n)
        temp[1].sort()
print(f'Os valores pares são: {temp[0]}\nOs valores são impares: {temp[1]} ')