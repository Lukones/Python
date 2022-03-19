# Um programa que vai analisar se existe letra O na frase #

frase = str(input('Por favor, digite uma frase: ')).upper().strip()
print(f'A letra O apareceU {frase.count("O")} vezes na frase: ')
print(f'A primeira letra O apareceu na posição {(frase.find("O")+1)}')
print(f'A última letra O apareceu na posição {(frase.rfind("O")-1)}')
