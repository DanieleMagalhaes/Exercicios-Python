numero = int(input('\nDigite um número inteiro: '))
if numero%2 == 0:
    print('\033[1;33mO número {} é PAR! \33[m \n' .format(numero))
else:
    print('\033[1;32mO número {} é IMPAR! \33[m \n' .format(numero))

