print('\nDIGITE UM VALOR PARA CADA RETA (A,B,C) PARA SABER SE É POSSÍVEL FORMAR UM TRIANGULO.')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
if a < b + c and b < a + c and c < a + b:
    print('\n\33[1;33mAs retas {}, {} e {} formam um triangulo! \33[m' .format(a,b,c))
else:
    print('\n\33[1;31mAs retas {}, {} e {} NÃO formam um triangulo! \33[m' .format(a,b,c))
print ('-'*50)
