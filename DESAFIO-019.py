# Um programa que vai determinar se a cidade que a pessoa digitou começa com a palavra RIO#

c = str(input('Em que cidade você nasceu? ')).strip()
print (f"Essa cidade começa com a palavra Rio: {c[:5].upper() == 'RIO'}")