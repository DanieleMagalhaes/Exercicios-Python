#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
totalCedula = 0
cedula = 50
print('='*50)
print('{:^55}'.format('\33[34mBANCO GEEK\33[m'))
print('='*50)
valor = int(input('Qual o valor do saque: '))
total = valor
while True:
    if total >= cedula:
        total = total - cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de \33[32m{totalCedula}\33[m cédulas de R$\33[32m{cedula}\33[m')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('='*50)
print('Volte sempre ao Banco Geek! Tenha um bom dia!')