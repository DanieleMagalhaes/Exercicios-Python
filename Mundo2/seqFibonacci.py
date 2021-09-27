print('='*60)
print('SEQUENCIA FIBONACCI')
print('='*60)
total = int(input('Quantos termos gostaria de mostrar? '))
termo1 = 0
termo2 = 1
cont = 3 #começa no 3 pq já mostrei 1º e 2º termo
if total != 0:
    print('\33[32m{}\33[m'.format(termo1), end=" → ")
    print('\33[32m{}\33[m'.format(termo2), end=" → ")
    while cont <= total:
        termo3 = termo2 + termo1
        print('\33[32m{}\33[m'.format(termo3), end=" → ")
        termo1 = termo2
        termo2 = termo3
        cont += 1
    print('FIM')
else:
    print('\33[31mQuantidade inválida!\33[m')
print('='*60)