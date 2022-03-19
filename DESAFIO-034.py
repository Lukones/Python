from datetime import date

alista = float(input('Por favor digite o ano de nascimento: '))
resul = (date.today().year - alista)
n = 18 - resul
x = resul-18
foi = date.today().year - x
vai = date.today().year + n
if resul < 18:
    print(f'Não chegou sua hora de se alista, faltam {n:.0f} ano(s) para poder')
    print(f'Seu alistamento será no ano de {vai:.0f}.')
elif resul == 18:
    print('Este é o ano do seu alistamento por gentileza dirija se para junta militar')
else:
    print(f'Você já deve ter se alistado no ano de {foi:.0f}, caso não, corra pois você está atrasado {x:.0f} ano(s)')

