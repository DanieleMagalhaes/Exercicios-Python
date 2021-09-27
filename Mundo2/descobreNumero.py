from random import randint
from time import sleep
computador = randint(0,10)
print('='*60)
print('\33[32mVou pensar em um número entre 0 e 10. Tente adivinhar!\33[m')
print('='*60)
jogador = int(input('Qual número eu pensei? '))
print('\33[32mPROCESSANDO...\33[m')
sleep(2)
vez = 1
while jogador != computador:
    print('\n\33[34mVocê errou.\33[m Tente novamente!')
    jogador = int(input('Qual número eu pensei? '))
    vez += 1
print('\33[36m\nParábens! Você acertou na {}ª tentativa, o nº escolhido foi {}.\33[m'.format(vez,computador))
print('='*60)