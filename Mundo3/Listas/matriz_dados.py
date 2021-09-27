matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
soma = somaPar = somaCol = maior = 0
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        soma += matriz[l][c] #soma todos dos valores
        if matriz[l][c] %2 ==0: #soma os pares
            somaPar += matriz[l][c]
        if matriz[1][c] == matriz[1][0]: #soma 2ª linha
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
    somaCol += matriz[l][2] #soma 3ª coluna
print('============ MATRIZ 3 X 3: =============\n')
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[ {matriz[l][c]:^4}]', end=' ') #: 4 casas decimais ^ centralizado
    print()
print('='*50)
print(f'A soma dos valores da matriz é: {soma}')
print(f'A soma dos valores PARES da matriz é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaCol}')
print(f'O maior valor da segunda linha é: {maior}')