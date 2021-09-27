from datetime import date
anoAtual = date.today().year
print('-'*40)
anoNascimento = int(input('Ano de nascimento: '))
idade = anoAtual - anoNascimento
if idade < 18:
    tempo = 18 - idade
    alistamento = anoAtual + tempo
    print('\33[32mVocê ainda vai se alistar ao Serviço Militar em {}. Faltam {} ano(s). \33[m' .format(alistamento, tempo))
elif idade > 18:
    tempo = idade - 18
    alistamento = anoAtual - tempo
    print('\33[33mVocê passou {} ano(s) do prazo para se alistar ao Serviço Militar. Seu alistamento foi em {}.\33[m'.format( tempo, alistamento))
else:
    print('\33[34mEste ano você precisa se alistar! Não se esqueça! \33[m')
print('-'*40)