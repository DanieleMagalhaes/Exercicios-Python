#TUPLA É IMUTÁVEL 
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)       #mostra todos
print(lanche[1])    #mostra Suco
print(lanche[-1])   #mostra o último
print(lanche[1:])   #mostra do Suco até o último
print(f'O comprimento da tupla Lanche é: {len(lanche)}')  
print(f'Mostra em ordem: {sorted(lanche)}\n')   #mostra em ordem (mas não altera a tupla)

#USANDO O FOR
for comida in lanche:
    if comida == 'Suco':
        print('\33[32mEu bebi Suco!\33[m')
    else:
        print(f'\33[32mEu comi {comida}\33[m')
print('\33[33mNossa, eu comi pra caramba!\33[m\n')

#OUTRA FORMA DE USAR O FOR >> MOSTRA A POSIÇÃO
for cont in range(0, len(lanche)):
    print(f'\33[32m{cont}º eu comi {lanche[cont]}\33[m')
print('\33[33mNossa, eu comi pra caramba!\33[m\n')

#OUTRA FORMA DE USAR O FOR >> MOSTRA TBM A POSIÇÃO
for posicao, comida in enumerate(lanche):
    print(f'\33[32mComerei {comida} na posição: {posicao}\33[m')
print('\33[33mNossa, eu comi pra caramba!\33[m\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'Tupla A:{a}')
print(f'Tupla B:{b}')
print(f'Tupla C:{c}')
print(f'Comprimento de C (A+B): {len(c)}')
print(f'Quantas vezes aparece o 5: {c.count(5)}')
print(f'Em que posição está o 8: {c.index(8)}')
print(f'Em que posição está o 5: {c.index(5,2)}\n')

pessoa = ('Daniele', 33, 'Feminino', 58)
print(f'\33[36mNome:{pessoa[0]}, Idade: {pessoa[1]}, Sexo: {pessoa[2]}, Peso: {pessoa[3]}\33[m')
#del(pessoa) >> apagar toda (somente, um elemento não)