# Um programa que cálcula quantos m² uma parede tem e o tanto de tinta que vai gastar para poder pintar ela #

a = float(input('Por favor me informe a altura da parede: '))
l = float(input('Por favor me informe a largura da parede: '))
t = float(input('Por favor me informe o rendimento da tinta a cada L/m²: '))
area = a*l
tinta = area/t
print(f'Certo, calculamos que você irá gastar {tinta:.1f}L de tinta para poder pintar a parede de {area}m²')
