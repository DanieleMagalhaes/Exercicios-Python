numeros = list()
pares = list()
impares = list()
print('='*50)
while True:
    n = int(input("Digite um valor: "))
    numeros.append(n)
    if n%2 == 0:   #ou posso fazer usando o for 
        pares.append(n)
    else:
        impares.append(n)
    resp = input("Quer continuar? [S/N]: ").strip().upper()[0]
    while resp not in 'SN':
        resp = input("Opção inválida! Quer continuar? [S/N]: ").strip().upper()[0]
    if resp in 'N':
        break
print('='*50)
print(f'Lista completa: {numeros}')
print(f'Lista Pares: {pares}')
print(f'Lista Impares: {impares}')

#usando o for ficaria:
#primeiro não precisaria jogar cada elemento em n
#numeros.append(int(input("Digite um valor: ")))
#for i, n in enumerate(numeros):
#    if n%2 == 0:   #ou posso fazer usando o for 
#        pares.append(n)
#    else:
#        impares.append(n)