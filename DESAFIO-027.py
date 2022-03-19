# Um programa que verifica se um ano é bissexto ou não #

from time import sleep
from datetime import date
ano = int(input('Digite um ano: '))
print('Verificando se é um ano Bissexto')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print(f'O ano {ano} é um ano Bissexto')
else:
    print(f'O ano {ano} não é um ano Bissexto')
