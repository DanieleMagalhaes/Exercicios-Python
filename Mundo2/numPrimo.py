#uma divisão com quociente menor que o divisor e o resto diferente de zero. Neste caso o número é primo.
numero = int(input('\nDigite um número: '))
divisiveis = 0
print('='*60)
for c in range(1,numero+1):
    if (numero % c == 0) : #se o numero for divisível pelo contador
        print('\33[32m', end='')
        divisiveis += 1
    else:
        print('\33[31m', end='')
    print('{}' .format(c), end=' ')
print('\n\33[mO número {} foi dividido {} vezes.' .format(numero,divisiveis))
if divisiveis == 2:
    print('E por isso ele é \33[33mPRIMO.\33[m')
else:
    print('E por isso ele \33[33mNÃO É PRIMO\33[m')
print('='*60)