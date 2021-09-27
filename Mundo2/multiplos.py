soma = 0
cont = 0
for c in range(3,500, 2):
    if (c % 3 == 0):
        cont = cont + 1
        soma += c
print('\nSoma dos \33[33m{}\33[m números IMPARES que são MULTIPLOS de 3, entre 1 e 500 é: \33[33m{}\n\33[m'.format(cont,soma))
