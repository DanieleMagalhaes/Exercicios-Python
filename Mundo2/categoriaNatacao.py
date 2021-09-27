from datetime import date
print('\nDIGITE SEU ANO DE NASCIMENTO PARA VERIFICAR QUAL SUA CATEGORIA.')
print('-'*62)
anoAtual = date.today().year
anoNascimento = int(input('Ano de nascimento: '))
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Categoria: \33[32mMIRIM\33[m')
elif idade <= 14:
    print('Categoria: \33[33mINFANTIL\33[m')
elif idade <= 19:
    print('Categoria: \33[34mJUNIOR\33[m')
elif idade <= 20:
    print('Categoria: \33[35mSÊNIOR\33[m')
else:
    print('Categoria: \33[36mMASTER\33[m')
print('-'*62)
