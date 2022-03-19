p = float(input('Me informe seu peso: '))
a = float(input('Me informe sua altura: '))
imc = p/(a**2)
print(f'SEU IMC {imc:.1f}')
if imc <= 18.50:
    print('Você se encontra ABAIXO DO PESO')
elif imc > 18.51 and imc <= 25.00:
    print('Você se encontra no PESO IDEAL')
elif imc > 25.01 and imc < 30.00:
    print('Você se encontra SOBREPESO')
elif imc > 30.01 and imc < 40.00:
    print('Você se encontra com OBESIDADE')
else:
    print('Você se encontra com OBESIDADE MÓRBIDA')
