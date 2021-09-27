from time import sleep
while True:
    cont = 1
    valor = int(input('\nDigite um valor para ver sua tabuada: '))
    if valor < 0:
        break
    print('-' * 12)
    while cont <= 10:
        print(f'\33[34m{valor}\33[m x \33[34m{cont:2}\33[m = \33[32m{valor*cont}\33[m ')
        cont += 1
    print('-' * 12)
print('\33[33mFINALIZANDO...\33[m\n')
sleep(1)