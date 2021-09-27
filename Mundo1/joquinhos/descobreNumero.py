from random import randint
from time import sleep # para dar um tempo antes de executar outra ação
computador = randint(0,5) #faz o PC sortear um inteiro entre 0 e 5
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print("\nPROCESSANDO...")
sleep(2) #tempo de 2 segundos
if jogador == computador:
   print('Parabéns, você conseguiu me vencer!!! O número escolhido foi o: {}!'.format(computador))
else:
   print('Desculpe, mas eu venci! Eu pensei no número {} e não no {}.'.format(computador,jogador))
print('-=-'*20)
