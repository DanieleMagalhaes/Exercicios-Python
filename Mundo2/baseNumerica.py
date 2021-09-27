print('-'*40)
numero = int(input('Digite um número inteiro: '))
print('\nEscolha uma das bases para conversão: ')
opcao = int(input('\33[32m[ 1 ] - BINÁRIO\33[m \n\33[33m[ 2 ] - OCTAL\33[m \n\33[34m[ 3 ] - HEXADECIMAL\33[m \nDigite sua opção: '))
print('-'*40)
if opcao == 1:
    print('\33[32m{} na base 2 é: {}\33[m'.format(numero,bin(numero)[2:])) #binario bin(n)
elif opcao == 2:
    print('\33[33m{} na base 8 é: {}\33[m'.format(numero,oct(numero)[2:])) #octal oct(n)
elif opcao == 3:
    print('\33[34m{} na base 16 é: {}\33[m'.format(numero,hex(numero)[2:])) #hexadecimal hex(n)
else:
    print('\33[31mOpção inválida! Tente novamente.\33[m')
print('-'*40)