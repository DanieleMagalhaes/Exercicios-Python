valor = int(input('\nDigite um valor para ver sua tabuada: '))
print('-' * 12)
for c in range (1,11):
    print('\33[34m{}\33[m x \33[34m{:2}\33[m = \33[32m{}\33[m '.format(valor, c, valor*c))
print('-' * 12)
