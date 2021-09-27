from math import pow
print('-'*50)
print('CALCULO DE INDICE DE MASSA CORPORAL')
print('-'*50)
peso = float(input('Digite seu peso (kg):  '))
altura = float(input('Digite sua altura (m): '))
imc = peso / pow(altura,2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5: 
    print('Resultado: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Resultado: PESO IDEAL')
elif 20 <= imc < 30:
    print('Resultado: SOBREPESO')
elif 30 <= imc < 40:
    print('Resultado: OBESIDADE')
else:
    print('Resultado: OBESIDADE MORBIDA')
print('-'*50)
    

