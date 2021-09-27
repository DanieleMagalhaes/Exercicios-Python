numero1 = int(input('\nDigite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
print('-'*40)
if numero1 > numero2:
    print('\33[32mO 1º valor é maior!\33[m')
elif numero1 < numero2:
    print('\33[33mO 2º valor é maior!\33[m')
else:
    print('\33[31mNão existe valor maior, os dois valores são iguais.\33[m')
print('-'*40)