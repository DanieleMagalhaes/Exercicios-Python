frase = str(input('\nDigite uma frase: ')).upper().strip()
print('Na frase existem {} letras "A"' .format(frase.count('A'))) #contar quantas letras 'a' tem na frase
print('A letra A aparece pela 1ª vez na posição: {}' .format(frase.find('A')+1)) # para pular o indice 0 para usuario
print('A letra A aparece pela última vez na posição: {}' .format(frase.rfind('A')+1)) #R rigth a partir do lado direito
