# BASE DECIMAL = 0 1 2 3 4 5 6 7 8 9 = BASE 10 =
# PARA CONVERTER DIVIDIRMOS POR 10 ATÉ CHEGAR ONDE N POSSA DIVIDIR, E O RESTO DA DIVISAO PEGAMOS DE TRAS PARA FRENTE
# BASE BINÁRIA = 0 1 = BASE 2 =
# PARA CONVERTER DIVIDIRMOS POR 2 ATÉ CHEGAR ONDE N POSSA DIVIDIR, E O RESTO DA DIVISAO PEGAMOS DE TRAS PARA FRENTE
# BASE OCTAL = 0 1 2 3 4 5 6 7 = BASE 8 =
# PARA CONVERTER DIVIDIRMOS POR 8 ATÉ CHEGAR ONDE N POSSA DIVIDIR, E O RESTO DA DIVISAO PEGAMOS DE TRAS PARA FRENTE
# BASE HEXADECIMAL =  0 1 2 3 4 5 6 7 8 9 A B C D E F = BASE 16 =
# PARA CONVERTER DIVIDIRMOS POR 16 ATÉ CHEGAR ONDE N POSSA DIVIDIR, E O RESTO DA DIVISAO PEGAMOS DE TRAS PARA FRENTE

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
  [ 1 ] Converter para BINÁRIO
  [ 2 ] Converter para OCTAL
  [ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin (num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {(hex(num)[2:])}')
else:
    print('Opção Inválida! Tente novamente.')






