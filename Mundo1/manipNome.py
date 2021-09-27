nome = str(input('\nDigite seu nome completo: ')).strip()
print('-' * 40)
#print('Nome tem Silva: '{})
print('\nNome com letras maiúsculas: {}' .format(nome.upper()))
print('Nome com letras mínusculas: {}' .format(nome.lower()))
print('Seu nome completo tem {} letras' .format(len(nome) - nome.count(' ')))
print('Tem "Silva" como sobrenome? : {} '.format('SILVA' in nome.upper()))
separa = nome.split()
print (separa)
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0],len(separa[0])))
print('Seu último nome é {} e tem {} letras.' .format(separa[-1],len(separa[-1])))# -1 ultimo, -2 penultimo ...

cidade = str(input('\nDigite da sua cidade: ')).strip()
print('Sua cidade começa com "Santo": {} '.format(cidade[:5].upper() == 'SANTO')) #jogo tudo pra maiusculo e texto por maiusculo



