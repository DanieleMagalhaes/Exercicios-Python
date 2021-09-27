distancia = float(input('\nQual a distancia da sua viagem? '))
print('\nDistancia percorrida foi {:.2f} km. '.format(distancia))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
#passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45 >>> OU SIMPLIFICADO
print('Valor da passagem \33[1;33m{:.2f} reais \33[m\n'.format(passagem))