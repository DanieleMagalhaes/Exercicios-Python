tempo = int(input('\nQuantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('-'*30)

#condição simplificada
tempo = int(input('Quantos anos você tem? '))
print('Você está novo' if tempo <= 40 else 'Você está velho')
print ('-'*30)

nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
nota3 = float(input('Digite a sua 3ª nota: '))
nota4 = float(input('Digite a sua 4ª nota: '))
media = (nota1+nota2+nota3+nota4) / 4
if media <= 5:
    print('Sua média foi: {:.1f}. Infelizmente você foi reprovado!' .format(media))
else:
    print('Sua média foi: {:.1f}. Parabéns você foi aprovado!' .format(media))
print('--FIM--')