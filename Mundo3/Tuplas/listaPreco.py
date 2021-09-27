print('-'*52)
print(f'\33[33m{"LISTAGEM DE PREÇOS":^52}\33[m') #:^50 centralizado 40 caracteres
print('-'*52)
lista = ('Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.90,
    'Mochila', 120.90,
    'Kit Canetas', 22.90,
    'Livro', 34.90)
for posicao in range(len(lista)): # para cada posicao do tamanho(lista)
    if posicao % 2 ==0: #se a posição for par então será o nome do produto
        print(f'{lista[posicao]:.<40}', end='') #:<40 alinhado direita 40 caracteres
    else:               #se a posição for impar então será o preço
        print(f'R$\33[32m{lista[posicao]:>7.2f}\33[m') #:>10 alinhado esquerda 10 carac e 2.f para ficar com 2 casas decimais
