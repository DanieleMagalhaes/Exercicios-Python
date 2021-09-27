valor = cont = soma = media = 0
maior = menor = 0
opcao = 'S'
print('='*50)
while opcao in 'S':
    valor = int(input('Digite um valor: '))
    opcao = str(input('Quer continuar \33[32m[S/N]\33[m: ')).upper().strip()[0]
    cont += 1
    soma += valor
    if cont == 1: #começa verif o 1º numero
        maior = valor
        menor = valor
    else: #se nao for o 1º
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor       
media = soma / cont
print('\nVocê digitou {} números. A média foi: {}'.format(cont, media))
print('O maior valor foi: {} e o menor foi: {}'.format(maior, menor))
print('='*50)