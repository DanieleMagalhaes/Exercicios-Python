print('-'*52)
print(f'\33[33m{"CONTADOR DE VOGAIS":^52}\33[m') #:^50 centralizado 40 caracteres
print('-'*52)
lista = (str(input('Digite uma palavra: ')).upper().strip(), 
        str(input('Digite outro palavra: ')).upper().strip(), 
        str(input('Digite mais uma palavra: ')).upper().strip(),
        str(input('Digite a última palavra: ')).upper().strip())
print(f'Tupla: \33[32m{lista}\33[m')
for palavra in lista: # para cada palavra na lista
    print(f'\nNa palavra \33[32m{palavra}\33[m contém: ', end='')
    for letra in palavra: # para cada letra da palavra
        if letra.upper() in 'AEIOUÁÉÍÓÚÂÊÃÕ': # se letra contem AEIOU...
            print(f'\33[33m{letra}\33[m', end=' ')
