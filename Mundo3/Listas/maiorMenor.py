print('-'*50)
lista = []
maior = menor = 0
for l in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {l}: '))),
    if l == 0:
        maior = menor = lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        if lista[l] < menor:
            menor = lista[l]
print('-'*50)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi: {maior} na posição: ', end='')
for indice, v in enumerate(lista): #for para posição
    if v == maior:
        print(f'{indice}', end=' ')
print()
print(f'O menor valor digitado foi: {menor} na posição: ', end='')
for indice, v in enumerate(lista): #for para posição
    if v == menor:
        print(f'{indice}', end=' ')
print()
print('-'*50)
