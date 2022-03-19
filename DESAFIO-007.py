# Um programa que converte o valor do real para dólar e vice-versa #

dol = 5.04
n = float(input('Vamos agora converter o real em dólar, me informe o valor em real: R$ '))
x = n/dol
print(f'Parabéns agora você possue: ${x:.2f} dólar(es)')

print("-.-" * 50)

w = float(input('Vamos agora converter o dólar em real, me informe o valor em dólar: $ '))
print(f'Parabéns agora você possue: R${w*dol:.2f} real(is)')