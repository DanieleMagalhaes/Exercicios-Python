numeros = [[],[]]
valor = 0
cont = 1
print('='*50)
for c in range(1,8):
    valor = int(input(f'Digite o {cont}º número: '))
    cont += 1
    if valor % 2 ==0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('='*50)
numeros[0].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares digitados foram: {numeros[1]}')
print(f'Lista Completa: {numeros}')