print('-'*50)
numero = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if  0 < num <=20:
        break
    print('Tente novamente.', end=' ')
print('-'*50)
print(f'\33[34mO número que você digitou é\33[m {numero[num]}')
print('-'*50)

 