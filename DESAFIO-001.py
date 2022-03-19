# Um programa que faz uma análise na letra digitada! #

tecla = input('Digite uma letra: ')

print('Seu tipo primitivo é: {} -'.format(tecla), type(tecla))

print('Seu tipo tem somente letras: {} -'.format(tecla), tecla.isalpha())

print('Estão em letra maiúscula: {} -'.format(tecla), tecla.isupper())

print('Seu tipo tem números e letras:', tecla.isalnum())

print('Seu tipo so tem números:', tecla.isnumeric())

print('Tem caracteres, letras, números ou é vazia:', tecla.isascii())

print('Seu tipo é decimal:', tecla.isdecimal())

print('São digitos:', tecla.isdigit())

print('Não é uma palavra reservada do python:', tecla.isidentifier())

print('São minúscula:', tecla.islower())

print('Esse pode ser impresso:', tecla.isprintable())

print('Seu tipo só tem espaço: ', tecla.isspace())

print('Começa com letra maiúscula: ', tecla.istitle())
