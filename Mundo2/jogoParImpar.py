from random import randrange
from time import sleep
print('='*50)
print('\33[1;32mVAMOS JOGAR PAR OU IMPAR:\33[m')
print('='*50)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    opcao = str(input('Par ou Impar? \33[1;32m[P/I]\33[m: ')).upper().strip()[0]
    while opcao not in 'PpIi':
        opcao = str(input('\33[31mOpção inválida.\33[m Por favor, Par ou Impar? \33[1;32m[P/I]\33[m: ')).strip().upper()[0]
    computador = randrange(10)
    print('='*50)
    print(f'\33[1;36mVocê:\33[m {jogador}       \33[1;34m      VS      \33[m ', end='')
    print(f'\33[1;36m      Computador:\33[m {computador}')
    print('='*50)
    soma = jogador + computador
    if (soma %2 == 0):
        print('\33[1;36mTotal deu PAR!\33[m', end=' ')
        if opcao in 'Pp' :
            print('\33[1;33mVocê VENCEU!\33[m')
            sleep(1)
            vitoria += 1
        elif opcao in 'Ii':
            print('\33[1;31mVocê PERDEU!\33[m')
            break
    else:
        print('\33[1;36mTotal deu IMPAR!\33[m', end=' ')
        if opcao in 'Ii':
            print('\33[1;33mVocê VENCEU!\33[m')
            sleep(1)
            vitoria += 1
        elif opcao in 'Pp':
            print('\33[1;31mVocê PERDEU!\33[m')
            break
    print('Vamos jogar novamente...')
    print('='*50)
if vitoria == 0:
    print(f'\33[1;32mGAME OVER!\33[m \33[1;33mInfelizmente você não venceu nenhuma vez.\33[m')
else:
    print(f'\33[1;32mGAME OVER! Você venceu\33[m \33[1;33m{vitoria}\33[m \33[1;32mvez(es).\33[m')
print('='*50)
