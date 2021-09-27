matriz = [[0, 0, 0], [0, 0, 0] , [0, 0, 0]]
print('='*60)
#para guardar o valores na matriz
for l in range(0,3): # linha
    for c in range(0,3): # coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
print('======== MATRIZ 3X3: =========\n')
#para imprimir 
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]', end=' ')
    print() #quebra de linha após imprimir as três colunas
print('='*30)