from time import sleep
print('************************** BANCO LUKONES **************************')
print('NOTAS DÍSPONIVEIS [R$ 50], [R$ 20], [R$ 10], [R$ 01]')
x = int(input('Digite o valor a ser sacado: '))
print('*******************************************************************')
print('Contando notas...')
sleep(2)
nota50 = 50
qtde50 = x // nota50
rstde50 = x % nota50
nota20 = 20
qtde20 = rstde50 // nota20
rstde20 = x % nota20
nota10 = 10
qtde10 = rstde20 // nota10
rstde10 = x % nota10
nota01 = 1
qtde01 = rstde10 // nota01
rstde01 = x % nota01
while True:
    if rstde50 == 0:
        print(f'O total a sair e de {qtde50} cédulas de R$50')
        break
    if rstde50 != 0:
        print(f'O total a sair e de {qtde50} cédulas de R$50')
        if rstde20 == 0:
            print(f'O total a sair e de {qtde20} cédulas de RS20')
            break
    if rstde20 != 0:
        print(f'O total a sair e de {qtde20} cédulas de R$20')
        if rstde10 == 0:
            print(f'O total a sair e de {qtde10} cédulas de R$10')
            break
    if rstde10 != 0:
        print(f'O total a sair e de {qtde10} cédulas de R$10')
        if rstde01 == 0:
            print(f'O total a sair e de {qtde01} cédulas de RS1')
            break
    if rstde01 != 0:
        print(f'O total a sair e de {qtde01} cédulas de R$1')
        break
print('{:-^50}'.format(' RETIRE O DINHEIRO '))
print('{:-^50}'.format(' VOLTE SEMPRE AO BANCO LUKONES  '))
