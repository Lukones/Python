from time import sleep
print(f'{" LOJAS MESSIAS ":=^40}')
p = float(input('Digite o preço do produto por gentileza: '))
d10 = p-(p*(10/100))
d5 = p-(p*(5/100))
d20 = p+(p*(20/100))
parcela = p / 2
print('Digite forma de pagamentos')
print('A', '- Dinheiro')
print('B', '- Cartão a vista')
print('C', '- Cartão 2x')
print('D', '- Cartão 3x')
x = input('Digite qual opção de pagamento: ').upper()
if x == 'A':
    print(f'O valor a ser pago tem 10% de desconto, o valor a ser pago é de R${d10}')
elif x == 'B':
    print(f'O valor a ser pago tem 5% de desconto, o valor a ser pago é de R${d5}')
elif x == 'C':
    print(f'O valor a ser pago não tem desconto, o valor a ser pago é de R${p}')
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif x == 'D':
    totparc = int(input('Quantas parcelas? '))
    parcela2 = d20 / totparc
    print(f'O valor a ser pago contem juros, o valor a ser pago é de R${d20}')
    print(f'Sua compra parcelada em {totparc}X de R${parcela2:.2f} aplicado juros')
else:
    print('Opção invalida de pagamento')
print('Processando pagamento...')
sleep(2)
print('Muito obrigado pela sua compra')