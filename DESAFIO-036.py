from datetime import date
ano = int(input('Digite o ano de nascimento do competidor: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print(f'O competidor e da categoria MIRIM, falta {10 - idade} ano(s) para ele subir para proxima')
elif idade <= 14:
    print(f'O competidor e da categoria INFANTIL, falta {15 -idade} ano(s) para ele subir para proxima')
elif idade <=19:
    print(f'O competidor e da categoria JUNIOR, falta {20 - idade} ano(s) para ele subir para proxima')
elif idade == 20:
    print(f'O competidor e da categoria SÊNIOR, falta {21 - idade} ano(s) para ele subir para proxima')
else:
    print('O competidor está na categoria MASTER!!')
