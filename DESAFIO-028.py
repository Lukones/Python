# Um programa que determina o maior e o menor nº dos informados
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um só mais um número: '))
#VERIFICANDO QUEM É MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#VERIFICANDO QUEM É O MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
