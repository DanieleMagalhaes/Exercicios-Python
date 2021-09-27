print('='*60)
maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Peso {}ª da pessoa: '.format(p)))
    if p == 1: # se for a primeira pessoa ela tem o maior e o menor peso
        maior = peso
        menor = peso
    else: # se for outras pessoas
        if peso > maior: # se o peso dela for maior que a outro, maior recebe o peso dela
            maior = peso
        if peso < menor: # se o peso dela for menor que a outro, menor recebe o peso dela
            menor = peso
print('\nO maior peso é: {}Kg'.format(maior))
print('O menor peso é: {}Kg'.format(menor))
print('='*50)