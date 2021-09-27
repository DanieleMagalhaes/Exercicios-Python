#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre: 
#A) Quantos números foram digitados. 
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
cont = 0
print('='*50)
while True:
    numeros.append(int(input("Digite um valor: ")))
    cont += 1
    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input("Opçao inválida! Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nForam digitados {cont} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros} ') 
if 5 in numeros:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não foi encontrado!")
print('='*50)
