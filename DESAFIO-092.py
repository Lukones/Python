def escreva(txt):
    print('*' * (len(txt) + 4) )
    print(f'  {txt}')
    print('*' * (len(txt) + 4) )

x = str(input('Digite uma palavra ou frase: '))
escreva(x)
