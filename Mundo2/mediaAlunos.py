nota1 = float(input('\nDigite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
nota3 = float(input('Digite a sua 3ª nota: '))
nota4 = float(input('Digite a sua 4ª nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('-'*40)
if nota1 or nota2 or nota3 or nota4 > 10:
    print('\33[1;31mERRO! Não aceitos valores acima de 10.\33[m')
else:
    print('\nSua média é: {:.1f} '.format(media))
    if media < 5.0:
        print('\33[31mVocê foi REPROVADO\33[m')
    elif 7 > media >= 5:
        print('\33[33mVocê está de RECUPERAÇÃO!\33[m')
    elif media >= 7.0:
        print('\33[32mVocê foi APROVADO!\33[m')
print('-'*40)