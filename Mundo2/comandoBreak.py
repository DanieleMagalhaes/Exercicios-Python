n = s = 0
cont = 0
while True: #loop infinito
    n =float(input('Digite um número: '))
    if n == 999:
        break #vai interromper e sair do loop
    s += n
    cont += 1
#print('A soma é: {} '.format(s))
print(f'Você digitou {cont} números e a soma deles é: {s:.2f}') #utilizando fstring
