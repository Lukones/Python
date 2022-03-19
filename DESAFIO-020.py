# Um programa que verifica se seu nome contém o nome Santos #

nome = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem Santos? {"santos" in nome.lower()}')