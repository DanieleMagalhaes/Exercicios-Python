print('-'*70)
# TESTE 1
for c in range(1,10):
    print(c, end=' ')
print('FIM FOR!')

cont = 1
while cont < 10:
    print(cont, end=' ')
    cont = cont + 1
print('FIM WHILE!')
print('-'*70)

# TESTE 2
for n in range(1,5):
    num = int(input('Digite um valor: '))
print('FIM FOR!\n')

valor = 1
while valor != 0:
    valor = int(input('Digite um valor: '))
print('FIM WHILE!\n')

#TESTE 3
numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um número: '))
    if numero !=0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vpcê digitou {} números PARES e {} números ÍMPARES.\n'.format(par,impar))