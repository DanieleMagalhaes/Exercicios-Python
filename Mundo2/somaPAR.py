print('-'*60)
soma = 0 #inicialize fora do FOR
cont = 0
for c in range(1,7):
    valor = int(input('Digite um valor: '))
    if (valor % 2 == 0):
        soma += valor
        cont +=1
print('\nVocê informou {} número(s) PARES e a soma é: {} '.format(cont, soma))
print('-'*60)
