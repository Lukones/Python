# Um programa que vai dar um aumento para um determinado funcionário, sendo necessário informar o
# preço e a porcetagem #

x = float(input('Veja o aumento do seu funcionário!\nDigite o salário dele: R$'))
y = float(input('Digite agora a porcetagem: '))
p = x+(x*(y/100))
print(f'O salário do seu funcionário vai para: R${p:.2f}')