valorImovel = float(input('\nQual o valor do imóvel que deseja financiar? '))
salario = float(input('Qual o seu salário mensal? '))
anos = int(input('Em quantos anos irá financiar o imóvel? '))
prestacao = valorImovel / (anos*12)
print('-'*50)
if prestacao < (30/100*salario):
    print('\33[32mSeu emprestimo foi aprovado!')
    print('Você ira pagar R${:.2f} por mês durante {} anos.\33[m' .format(prestacao,anos))
else:
    print('\33[31mSeu sáralio está muito abaixo para financiar este imóvel.\33[m')
    print('\33[31mInfelizmente seu emprestimo NÃO foi aprovado.\33[m')
print('-'*50)