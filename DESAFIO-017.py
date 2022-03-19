# Um programa que análisa o nome e faz alterações no mesmo #

nome = str(input('Digite seu nome: ')).strip()
print('Analiando seu nome...')
print(f'Seu nome em maiúsculas é {(nome.upper())}')
print(f'Seu nome em minúsculas é {(nome.lower())}')
print(f'Seu nome tem ao todo {(len(nome) - nome.count(" "))} letras')

# Os dois modos abaixos desconsideram o espaço e  conta as letras #
print(f'Seu primeiro nome tem {(nome.find(" "))} letras') # modo direto
separa = nome.split() #modo alternativo
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')


