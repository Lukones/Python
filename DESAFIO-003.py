# Um programa que solicita um nº qualquer e faz 3 cálculos diferentes para o nº escolhido:
# Dobro, Triplo e Raiz Quadrada #

n = int(input('Escolha um número: '))
print(f'O nº escolhido foi: {n}\nO dobro deste nº é: {n*2}\nO triplo deste nº é: {n*3}'
      f'\nA raiz quadrada deste nº é: {(n**(1/2)):.2f} ')

# Conseguimos usar o comando pow para realizar o cálculo da raiz #

n = int(input('Escolha um número: '))
print(f'O nº escolhido foi: {n}\nO dobro deste nº é: {n*2}\nO triplo deste nº é: {n*3}'
      f'\nA raiz quadrada deste nº é: {(pow(n, 1/2)):.2f} ')
