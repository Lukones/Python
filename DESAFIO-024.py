# Um programa que determina se o carro ta rápido ou devagar e da uma multa!

vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (vel-80) * 7
    print(f'Você deve pagar uma multa e R${multa:.2f}!')
    print('Pegue a multa e siga seu caminho, tome cuidado e respeite as leis de trânsito')
else:
    print('Dentro do limite estabelecido...')
    print('Tenha um bom dia! Dirija com segurança')
