from random import randint
from time import sleep
import emoji
item = ('PEDRA', 'PAPEL' , 'TESOURA') #definindo os itens da lista
print('-'*60)
print('\33[7;30;44mVamos jogar Jokempô?\33[m ')
print('-'*60)
print('Qual você escolhe? \n\33[33m[ 0 ] - PEDRA\33[m \n\33[32m[ 1 ] - PAPEL \33[m\n\33[34m[ 2 ] - TESOURA\33[m')
jogador = int(input('Sua jogada: '))
print('\n\33[1;36mJOKEEEEEENPO!\33[m\n')
sleep(2)
computador = randint(0,2)
print('-'*60)
print('\33[1;36mVocê:\33[m {}       \33[1;34m      VS      \33[m '.format(item[jogador]), end='')
print('\33[1;36m      Computador:\33[m {}'.format(item[computador]))
print('-'*60)
if jogador == computador:
    print(emoji.emojize('\33[35mEMPATAMOS! NINGUEM VENCEU\33[m! :relieved:',use_aliases=True))
elif jogador == 0 and computador == 1:
    print(emoji.emojize('\33[32mPAPEL\33[m EMBRULHA \33[33mPEDRA\33[m! EU TE VENCI!!! :stuck_out_tongue:',use_aliases=True))
elif jogador == 1 and computador == 0:
    print(emoji.emojize('\33[32mPAPEL\33[m EMBRULHA \33[33mPEDRA\33[m! VOCÊ VENCEU!!! :sweat_smile:',use_aliases=True))
elif jogador == 2 and computador == 0:
    print(emoji.emojize('\33[33mPEDRA\33[m QUEBRA \33[34mTESOURA\33[m! EU TE VENCI!!! :stuck_out_tongue:',use_aliases=True))
elif jogador == 2 and computador == 1:
    print(emoji.emojize('\33[34mTESOURA\33[m CORTA \33[32mPAPEL\33[m! VOCÊ VENCEU!!! :sweat_smile:',use_aliases=True))
elif jogador == 0 and computador == 2:
    print(emoji.emojize('\33[33mPEDRA\33[m QUEBRA \33[34mTESOURA\33[m! VOCÊ VENCEU!!! :sweat_smile:',use_aliases=True))
elif jogador == 1 and computador == 2:
    print(emoji.emojize('\33[34mTESOURA\33[m CORTA \33[32mPAPEL\33[m! EU TE VENCI!!! :stuck_out_tongue:',use_aliases=True))
else:
    print('\33[31mOpção inválida! Tente novamente.\33[m')
print('-'*60)
