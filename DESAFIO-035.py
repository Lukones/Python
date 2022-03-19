n1 = float(input('Por gentileza digite a primeira nota do aluno: '))
n2 = float(input('Por gentileza digite a segunda nota do aluno: '))
media = (n1+n2)/2
print(f'Sua media é {media}')
if media < 5.0:
    print('Infelizmente o aluno foi \033[4;34mREPROVADO\033[m')
elif 7 > media >= 5:
    print('Infelizmente o aluno está de \033[4;34mRECUPERAÇÃO\033[m')
else:
    print('Parabéns o aluno foi \033[4;34mAPROVADO\033[m')
