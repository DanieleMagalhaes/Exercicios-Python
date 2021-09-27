print('-'*50)
numeros = (int(input('Digite um número: ')), 
        int(input('Digite outro número: ')), 
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print('-'*50)
print(f'\33[32mOs números digitados foram: \33[m{numeros}')
print(f'\33[32mO número 9 apareceu {numeros.count(9)} vez(es).\33[m')
if 3 in numeros:
    print(f'\33[32mO número 3 apareceu na {numeros.index(3)+1}ª posição.\33[m')
else:
    print('\33[32mO número 3 não foi digitado.\33[m')
print(f'\33[32mNúmeros pares foram: \33[m', end='')
pares = 0
for n in numeros: #para cada n em numeros
    if n%2 == 0 and n != 0: #se pares e diferente de zero
        print(f'{n}', end=' ')
        pares +=1
if pares == 0: #se nao tiver nenhum par
    print('Nenhum')
