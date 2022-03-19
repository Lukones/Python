# Um programa que cálcula solicita notas de alunos e cálcula a média #

# Usar INT para nº redondos #
m = int(input('Escolha a nota de João para Matemática do 1 e 2º Bimestre: '))
p = int(input('Escolha a nota de João para Matemática do 3 e 4º Bimestre: '))
print(f'A sua média será de: {(m+p)/2}')

# Usar FLOAT para nº quebrados #

m = float(input('Escolha a nota de Maria para Matemática do 1º e 2º Bimestre: '))
p = float(input('Escolha a nota de Maria para Matemática do 3º e 4º Bimestre: '))
print(f'A sua média será de: {(m+p)/2}')

# O comando "int" não aceita números quebrados... Para isso usamos o "float", caso usarmos o float e quisermos
# ter o resultado redondo - pode utilizar ":.0f" para tirar as casas decimais #
