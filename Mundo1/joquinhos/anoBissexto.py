#De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.
#Prevalecem as últimas regras sobre as primeiras
from datetime import date
ano = int(input('\nQual ano você quer analizar? Coloque 0 para analizar o ano atual. '))
if ano == 0:
    ano =date.today().year #pega o ano atual da maquina
if ano%400== 0 or ano%4== 0 and ano%100!= 0:
    print('\33[1;33mO ano de {} é Bissexto!\33[m \n' .format(ano))
else:
    print('\33[1;31mO ano de {} NÃO é Bissexto!\33[m \n'.format(ano))