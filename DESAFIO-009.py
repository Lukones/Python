# Um programa que dá 5% de desconto em um valor que o cliente colocar #

preco = float(input('Estamos em promoção (-5%), digite o valor do preço do produto: R$ '))
porcem = 5
n = (preco-(preco*(porcem/100)))
print (f'O valor do desconto aplicado é R${preco - n:.2f}, sendo assim o valor a pagar é de R${n:.2f}.')