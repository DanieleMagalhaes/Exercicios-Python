print('='*60)
print('\33[32mGERADOR DE PROGRESSÃO ARITIMÉTICA\33[m')
print('='*60)
primeiro = int(input('Digite a 1º termo da P.A.: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10 #começa com 10 pq inicialmente serão 10 termos
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=" → ")
        termo += razao
        cont += 1
    print('\33[32mPAUSA\33[m')
    mais = int(input('\nQuantos termos a mais você gostaria de mostar: '))
print('\33[32mProgressão finalizada com {} termos mostrados.\33[m'.format(total))
