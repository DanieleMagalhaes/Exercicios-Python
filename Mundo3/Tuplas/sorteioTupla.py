from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = menor = 0
print(f'\n\33[34mOs números sorteados foram:\33[m ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n\33[34mO maior número é: \33[m {max(numeros)}', end='')
print(f'\n\33[34mO menor número é: \33[m {min(numeros)}', end='')
