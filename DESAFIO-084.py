ficha = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite nota 1: '))
    nota2 = float(input('Digite nota 2: '))
    media = (nota2 + nota1) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 40)
print('{:<4}{:<10}{:>8}'.format("No.", "NOME", "MEDIA"))
print('-=' * 40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_'* 35)
    opc = int(input('Mostrar nota individual? (999 paraa finalizar): '))
    if opc == 999:
        print('FINALIZADO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')