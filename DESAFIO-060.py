maior = 0
menor = 0
aux = 1
cont = 0
soma = 0
sair = 0
while sair != 'n':
    x = int(input('Digite um número: '))
    if x != '':
        o = str(input('Deseja continuar [S/N]: ')).lower().strip()
        if o == 'n':
            sair = 'n'
    if aux == 1:
        aux = 0
        maior = x
        menor = x
    if maior < x:
        maior = x
    if menor > x:
        menor = x
    cont += 1
    soma += x
    media = soma / cont
print(f'O total de números digitados foi de {cont},\na sua soma é de {soma} e a média {media}')
print(f'O número maior é {maior} e temos o menor que é {menor}')
