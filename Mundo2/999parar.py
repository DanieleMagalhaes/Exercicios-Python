num = soma = cont = 0 # todos recebem 0, pode simplificar assim.
num = int(input('Digite o número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite o número [999 para parar]: '))
print('\33[33m\nVocê digitou {} números e a soma entre eles é: {}\33[m'.format(cont, soma))
print('='*40)