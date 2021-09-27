print('\nDIGITE UM VALOR PARA CADA RETA (A,B,C) PARA SABER SE É POSSÍVEL FORMAR UM TRIANGULO.\n')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
if a < b + c and b < a + c and c < a + b:
    print('\n\33[1;33mAs retas {}, {} e {} formam um triangulo! \33[m' .format(a,b,c))
    #TIPO TRIANGULO
    if a == b == c:
        print('\nÉ um triângulo \33[35mEQUILÁTERO!\33[m')
    elif a != b and a != c and b!= c: # OU a != b != c != a 
        print('\nÉ um triângulo \33[34mESCALENO!\33[m')
    else:
        print('\nÉ um triângulo \33[32mISÓCELES!\33[m')
else:
    print('\n\33[1;31mAs retas {}, {} e {} NÃO formam um triangulo! \33[m' .format(a,b,c))
print ('-'*50)