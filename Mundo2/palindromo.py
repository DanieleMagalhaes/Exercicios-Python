print('='*50)
frase = str(input('Digite uma frase: ')).strip().upper()#desconsirera os espaços STRIP e colaca maiúsculo UPPER
palavras = frase.split() #dividir frase
junto = ''.join(palavras) #juntas as palavras sem espaço
inverso = ''
for letra in range(len(junto) - 1, -1 , -1): #da última letra(len - 1), até a primeira (-1), voltando de 1 em 1 (-1)
    inverso +=junto[letra]
print('Sua frase: {} e o inverso é: {}'.format(junto,inverso))

#OU MAIS FACIL (SEM FOR)
#criar variavel (inverso = junto[::-1]) do inicio ao fim -1

if inverso == junto:
    print('\33[32mSua frase é um Palindromo!\33[m')
else:
    print('\33[31mNÃO é um Palindromo!\33[m')
print('='*50)
