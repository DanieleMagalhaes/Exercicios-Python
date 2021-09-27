valor = float(input('\nDigite o valor da compra: '))
print('-'*60)
print('Escolha a condição de pagamento:\33[34m \n[ 1 ] - À VISTA (dinheiro/cheque) \n[ 2 ] - À VISTA (cartão débito) \n[ 3 ] - CARTÃO (em 2x sem juros) \n[ 4 ] - CARTÃO (em 3x ou mais)\33[m')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    print('-'*90)
    total = valor - (10/100*valor)
    print('Valor total a pagar: R${:.2f}'.format(total))
elif opcao == 2:
    print('-'*90)
    total = valor - (5/100*valor)
    print('Valor total a pagar: R${:.2f}'.format(total))
elif opcao == 3:
    print('-'*90)
    parcela = valor / 2
    print('Valor total a pagar: R${:.2f}, 2 parcelas de R${:.2f}'.format(valor, parcela))
elif opcao == 4:
    total = valor + (20/100*valor)
    parcela = int(input('Quantas parcelas? '))
    valorParcela = total / parcela 
    print('-'*90)
    print('Sua compra será parcelada em {}X de R${:.2f} com juros. Valor total da compra: R${:.2f} '.format(parcela, valorParcela, total))
else:
    print('\33[31mCondição inválida. Tente novamente!\33[m')
print('-'*90)