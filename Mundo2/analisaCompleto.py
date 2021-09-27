#pessoa = 1
somaIdade = 0
maiorMasc = 0
sexo = 'F'
mascVelho = 'Nenhum'
mulherVinte = 0
for pessoa in range (1,5):
    print('='*40)
    print('\33[34m{}ª PESSOA\33[m'.center(45).format(pessoa))
    print('='*40)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('\33[31mDado inválido.\33[m Por favor, informe seu sexo: ')).strip().upper()[0]
    pessoa += 1
    somaIdade += idade
    if sexo == 'M':
        if pessoa == 1:
            maiorMasc = idade
            mascVelho = nome
        else:
            if idade > maiorMasc:
                maiorMasc = idade
                mascVelho = nome
    else:
        if idade <= 20:
            mulherVinte += 1
media = somaIdade / 4
print('='*40)
print('\33[34mMédia das idades:\33[m \33[32m{}\33[m'.format(media))
print('\33[34mHomem mais velho é o \33[32m{}\33[m \33[34me ele tem\33[m \33[32m{} anos.\33[m'.format(mascVelho,maiorMasc))
print('\33[34mExistem \33[32m{} mmulheres\33[m \33[34mcom menos de 20 anos.\33[m'.format(mulherVinte))
print('='*40)
