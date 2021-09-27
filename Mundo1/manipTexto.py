texto = str(input('\nDigite uma frase: '))
print('-' * 40)
#fatiamento
print('Texto fatiado do indice 4 ao 12: {}' .format(texto[4:13]))
print('Texto fatiado do indice 9 ao 15, saltando de 2 em 2: {}' .format(texto[9:16:2])) 
print('Texto fatiado do indice 15 ao último: {}' .format(texto[15:])) 
print('Texto fatiado do indice 0 ao 8: {}' .format(texto[:8]))
print('Texto fatiado do indice 5 ao último, saltando de 3 em 3: {}' .format(texto[5::3]))
#analise
print('-' * 40)
print('O comprimento da frase é de {} letras'.format(len(texto))) #comprimento da string
print('Na frase existem {} letras "l"' .format(texto.count('l'))) #contar quantas letras 'l' tem na frase
print('Na frase existem {} letras "l" do índice O até 9.' .format(texto.count('l',0,10))) #contar quantas letras 'l' de O até 9
print('Encontrando "mundo" a partido do índice: {} '.format(texto.find('mundo'))) #caso não tenha apresenta -1
print('Existe a palavra "curso" na frase: {}' .format('curso'in texto))#vai dizer se existe o não a palavra desejada
#transformação
 
print('Nova frase: {}'.format(texto.replace('Python','JavaScript'))) #substitue a palavra, mas não salva 
texto = texto.replace ('Python','JavaScript') #para salvar
print('Frase letra maiúcula: {}' .format(texto.upper())) #coloca as letras com letras minúsculas para maiúsculas
print('Frase letra minúscula: {}' .format(texto.lower())) #coloca as letras com letras maiúsculas para minúsculas
print('Frase letra capitalizada: {}' .format(texto.capitalize())) #coloca as primeiras letras da frase em maiúscula
print('Frase como título: {}' .format(texto.title())) #coloca as primeiras letras da palavra em maiúscula
print('Frase correta: {}' .format(texto.strip())) #retira espaçamento inuteis no início e no fim da frase
print('Frase correta: {}' .format(texto.rstrip())) #retira espaçamento inuteis somente no fim da frase R "rigth"
print('Frase correta: {}' .format(texto.lstrip())) #retira espaçamento inuteis somente no início da frase L "left"
#dividir
print('-' * 40)
#SPLIT >> gera outra lista com cada palavra (separada por espaço) e cada indice será uma palavra da lista anterior 
frase = "Toda string em Python é imutável"
frase.split(" ")
['Toda', 'string', 'em', 'Python', 'é', 'imutável'] #'Toda' = 0, 'string' = 1, 'em' = 2, 'Python' = 3 ...
print(frase)
'-'.join(texto) #junta a lista anterior gerando uma unica cadeia de caracteres separados por -