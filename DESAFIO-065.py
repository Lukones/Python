print('=-='*30)
print('                                      LUKONES LOJA')
print('=-='*30)
menor = totalgasto = totalmil = cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o valor do produto: R$'))
    cont += 1
    totalgasto += preço
    if preço >= 1000:
        totalmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    dnv = ' '
    while dnv not in 'SsNn':
        dnv = str(input('Deseja cadastrar mais compras? [S/N] ')).strip().upper()[0]
    if dnv == 'N':
        break
print('=-=' * 30)
print('COMPRA FINALIZADA')
print('=-='*30)
print(f'O total gasto na sua compra foi de R${totalgasto}')
print(f'Existem no seu carrinho {totalmil} que custam mais de R$ 1000')
print(f'O menor valor de produto que existe em seu carinho é um(a) {barato} que custa {menor}.')