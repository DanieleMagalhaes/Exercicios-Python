import math #importa toda biblioteca de math (matemática)
num = int (input( '\nDigite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.' .format(num, math.ceil(raiz))) #ceil arredonda pra cima e floor pra baixo

# from math import sqrt, ceil >> importa somente a funcionalidade que irei usar
# raiz = sqrt(num) >> assim não preciso expecificar biblioteca math

import random
valor = random.randint(1,100) #gera um numero aleatório inteiro de 1 a 100
print('\nValor gerado: {}' .format(valor))

import emoji 
print(emoji.emojize("\nOlá, mundo! :earth_africa:\n", use_aliases=True))
