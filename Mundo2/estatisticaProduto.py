print('='*50)
print('\33[34mLOJA SOU BARATO\33[m')
somaCompra = produtoMil = 0
baratoPreco = 0
cont = 0
maisBarato = 'Nenhum'
while True:
    print('='*50)
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if preco > 1000:
        produtoMil += 1         # Soma total da compra
    cont += 1                   # contator para verif menor preço
    if cont == 1 or preco < baratoPreco: #Se for o 1º recebe o menor preço OU se for outro (2,3,4..) recebe o menor preço
        maisBarato = produto
        baratoPreco = preco
    somaCompra += preco    # Soma total da compra
    opcao = ' '
    while opcao not in 'SN':    
        opcao = str(input('\33[36mQuer continuar? [S/N]: \33[m')).strip().upper()[0]
    if opcao in 'N':
        break
print('='*50)
print(f'\33[34mTotal da compra foi: R$\33[m {somaCompra:10.2f} ')
print(f'\33[34mProduto(s) com preço acima de mil reais: \33[m {produtoMil}')
print(f'\33[34mProduto mais barato é:\33[m {maisBarato} \33[34mque custa:\33[m {baratoPreco}\n ')