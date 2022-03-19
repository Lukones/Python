# Um programa que realiza o calculo das razões trigonométricas #

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')

con = cos(radians(an))
print(f'O ângulo de {an} tem o CONSENO DE {con:.2F}')

tan = tan(radians(an))
print(f'O ângulo de {an} tem a TANGENTE de {tan:.2f}')


