# usando as strings e usando um macete de fatiamento:

frases = str(input('Digite uma frase: ')).strip().upper() #SEM MACETE
palavras = frases.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo! ')

# --------------------------------------------------------------- #
frasss = str(input('Digite uma frase: ')).strip().upper()
plavrass = frasss.split()
juntos = ''.join(plavrass)
inversos = juntos[::-1] #MACETE DE FATIAMENTO DE STRING
print('O inverso de {} é {}'.format(juntos, inversos))
if inversos == juntos:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo! ')


