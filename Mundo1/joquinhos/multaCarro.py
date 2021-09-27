print('-'*80)
km = int(input('\033[1;33mQual a velocidade do seu carro neste momento? \33[m'))
print('-'*80)
if km >= 81:
    print('Sua velocidade é de {}km/h. \033[1;31mVocê ultrapassou o limite permitido e será MULTADO!\033[m '.format(km))
    multa = (km - 80) * 7
    print('Você deve pagar uma multa no valor de: \033[1;31m{} reais\033[m.'.format(multa))
else:
    print('Sua velocidade é de {}km/h. Você está dentro do limite permitido! Siga sua viagem!' .format(km))
print('Tenha um bom dia! Dirija com segurança!\n')
