soma1 = cont1 = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont1 += 1
    soma1 += num
print(f'A soma dos {cont1} valores foi {soma1}!')
