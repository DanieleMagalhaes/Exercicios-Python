numero = int(input('\nDigite um número inteiro não negativo: '))
cont = numero
fatorial = 1
print('Calculando o fatorial de {}! = '.format(numero), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial = fatorial * cont
    cont = cont - 1
print('\33[32m{}\33[m'.format(fatorial))
print('-'*60)

#ou usando o método fatorial
from math import factorial
n = int(input('Digite um número inteiro não negativo: '))
f = factorial(n)
print('\33[32m{}! é: {}\33[m\n'.format(n, f))
