#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('='*50)
numeros = list()
while True: #enquanto for verdade faça
    n = int(input("\33[mDigite um valor: "))
    if n not in numeros: # se n nao estiver na lista numeros
        numeros.append(n)  # adiciona na lista
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado. Não será adicionado! ")
    opcao = str(input("\33[32mDeseja continuar [S/N]: \33[m")).strip().upper()[0] #primeira letra e transf. maiuscula
    while opcao not in 'NS': #enquanto opcao não for N ou S
        opcao = str(input("\33[31mOpção Inválida! \33[m \33[32mDeseja continuar [S/N]: \33[32m")).strip().upper()[0] 
    if opcao == 'N': #se for N 
        break        #interrompa e sai do loop while true
print('='*50)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
