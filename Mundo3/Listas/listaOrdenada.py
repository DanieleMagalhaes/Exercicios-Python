lista = []
print('='*50)
for v in range (0,5):
    n = (int(input("Digite um valor: ")))
    if v == 0 or n > lista[-1]: #se for maior que o ultimo valor (ou lista[len(lista)-1])
        lista.append(n)
        print('Adicionado ao final da Lista!')
    else:
        pos = 0 #para varrer as posições
        while pos < len(lista): #enquanto a posicao for menor que o tamanho da lista
            if n <= lista[pos]: #se n for menor ou igual ao valor daquela posicao
                lista.insert(pos,n) #insere naquela posicao
                print(f'Adicionado na posição {pos} da Lista!')
                break #interrompe pra inserir só uma vez
            pos += 1 #passa pra proxima posicao
print('='*50)
print(f'Os valores digitados em ordem foram: {lista}')