print('-'*60)
print('\33[35m[ F ] Feminino\33[m \n\33[32m[ M ] Masculino\33[m \n ')
sexo = str(input('Qual o seu sexo? ')).strip().upper()[0] # só pega a primeira letra
while sexo not in 'MF':
    sexo = str(input('\33[31mDados inválidos.\33[m Por favor, informe seu sexo: ')).strip().upper()[0]
print('\nSexo {} registrado com sucesso!'.format(sexo))
print('-'*60)