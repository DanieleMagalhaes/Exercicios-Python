salario = float(input('\nDigite o valor do seu salário: '))
aumento = 15/100 * salario
print('\nSeu salario teve um aumento de 15 porcento!\nNovo salário: R${:.2f} '. format(salario + aumento))