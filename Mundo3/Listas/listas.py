print('-'*60)
lista = ['Cadeira', 'Mesa', 'Casa']
print(f'Lista inicial: {lista}')
lista[2] = 'Carro' #alterar elemento 
lista.append('Lápis') #adiciona elemento na última posição
print(f'Lista adicionada: {lista}')
lista.sort() #coloca a lista em ordem alfabética
print(f'Lista em ordem: {lista}')
lista.sort(reverse=True) #coloca a lista em ordem reversa
print(f'Lista em ordem reversa: {lista}')
print(f'Esta lista tem {len(lista)} elementos.')
lista.insert(3, 'Livro') #insere na posição 3 e joga os demais uma posição a frente
print(f'Inserindo na posição: {lista}') 
lista.pop() #elimina o último elemento ou lista.pop(2) para elemento 2
print(f'Lista sem o último elemento: {lista}') 
lista.remove('Mesa') #remova a primeira ocorrencia do elemento sujerido
print(f'Removendo elemento: {lista}') 
if 'Borracha' in lista: #se não estiver na lista
    lista.remove('Borracha')
else: 
    print(f'Não achei o elemento: "Borracha"') 
print('-'*60)

# OUTRAS UTILIZADADES
valores = [] # lista vazia
valores.append(5)
valores.append(2)
valores.append(4)
for v in valores:
    print(f'{v} >> ', end='')
print('\n')
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): #for para posição
    print(f'Na posição {c} o valor é {v}.')
print('-'*60)

# MAIS UTILIZADADES
A = [2, 3, 4, 5]
B = A # igualando uma lista a outra
C = A[:] # C recebe todos os itens de A (cópia)
D = B.copy() # D recebe todos os itens de B (cópia) - aquivale d[0] = b[:]
B[1] = 9 
print(F'Lista A: {A}')
print(F'Lista B: {B}')
print(F'Lista C: {C}')
print(F'Lista D: {D}')
C[0] = 8
print(F'\nLista A: {A}')
print(F'Lista C: {C}')
