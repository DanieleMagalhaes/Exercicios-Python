real = float(input('\nDigite um valor em Reais: R$'))
peso = real * 13.63
iene = real * 19.80
dolar = real / 5.33
euro = real / 6.33
libra = real / 7.00
print('\nCONVERSOR DE MOEDAS')
print('-'*25)
print('Peso Argentino: $ {:.2f}' .format(peso))
print('Iene: ¥ {:.2f}' .format(iene))
print('Dolar: U$ {:.2f}' .format(dolar))
print('Euro: € {:.2f}' .format(euro))
print('Libra esterlina: £ {:.2f}' .format(libra))
print('-'*25)