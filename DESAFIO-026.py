# Um programa que calcula o gasto de gasolina, considerando o preço de R$ 7,00  #

g = float(input('Digite a distância em Km para saber o gasto final: '))
p = float(input('Seu carro é 1.0, 1.3, 1.6, 1.8...? Digite: '))

if p > 1.6:
    p1 = g / 8.5 # consumo medio para carros acima de 1.6
    p2 = p1 * 7
    print(f'O valor total a ser gasto como seu carro é: R${p2:.2f}')
else:
    p1 = g / 10.5  # consumo medio para carros abaixo de 1.6
    p2 = p1 * 7
    print(f'O valor total a ser gasto como seu carro é: R${p2:.2f}')