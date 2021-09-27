from random import randint
from time import sleep

print('='*30)
print(' '*5, ' JOGO MEGA SENA ', ' '*5)
print('='*30)
lista = []
jogos = []
total = 1
quantidade = int(input('Quantos jogos deseja sortear? '))
while total <= quantidade:  
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) # criar copia da lista
    lista.clear()
    total += 1
print()
print('-='*4, f' SORTEANDO {quantidade} JOGOS: ', '-=' *4)
for indice, j in enumerate(jogos):
    print(f'Jogo {indice+1}: {j}')
    sleep(1)
print()
print('-='*5, '< BOA SORTE! >','-='*5)