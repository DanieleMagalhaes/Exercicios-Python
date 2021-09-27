#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
idade = 0
somaIdade = somaMasc = somaFem20 = 0
print('-'*50)
while True:
    print('-'*50)
    print('\33[32mCADASTRE UMA PESSOA:\33[m')
    print('-'*50)
    idade = int(input('Idade: '))
    sexo = ' '
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('\33[31mDado inválido.\33[m Sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
        somaMasc += 1
    if sexo in 'F':
        if idade < 20 :
            somaFem20 += 1
    if idade >= 18:
        somaIdade += 1
    opcao = ' '
    while opcao not in 'SN':    
        opcao = str(input('\33[36mQuer continuar? [S/N]: \33[m')).strip().upper()[0]
    if opcao in 'N':
        break
print('-'*50)
print(f'\33[34mTotal de pessoas com mais de 18 anos:\33[m {somaIdade} ')
print(f'\33[34mTotal de pessoas do sexo masculino:\33[m {somaMasc}')
print(f'\33[34mTotal de mulheres com menos de 20 anos:\33[m {somaFem20}\n ')
