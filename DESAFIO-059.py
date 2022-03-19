n = int(input('Digite um número qualquer: '))
cont = 0
soma = n
while n != 999:
    n = int(input('Digite um número qualquer: '))
    cont += 1
    soma += n
    x = soma - 999
print(f'O total de números digitados foi de {cont} e sua soma é de {x}')
