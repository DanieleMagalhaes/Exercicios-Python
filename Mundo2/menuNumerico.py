from time import sleep
print('='*40)
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('='*40)
    print('O que você deseja fazer: \n\n[ 1 ] SOMAR \n[ 2 ] MULTIPLICAR \n[ 3 ] MAIOR \n[ 4 ] NOVOS NÚMEROS \n[ 5 ] SAIR DO PROGRAMA')
    opcao = int(input('\nOpção: '))
    print('='*40)
    if opcao == 1:
        soma = valor1 + valor2
        print('\33[32m{} + {} é: {}\33[m'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('\33[32m{} x {} é: {}\33[m'.format(valor1, valor2, mult))
    elif opcao == 3:
        maior = max(valor1,valor2)
        print('\33[32mO maior valor entre {} e {} é: {}\33[m'.format(valor1,valor2,maior)) 
    elif opcao == 4:
        print('\33[32mInsira novos valores:\33[m\n')
        valor1 = int(input('Digite o 1º valor: '))
        valor2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('\33[33mFinalizando... \33[m')
    else:
        print('\33[31mOpção inválida. Tente novamente\33[m')
    sleep(2)
print('='*40)