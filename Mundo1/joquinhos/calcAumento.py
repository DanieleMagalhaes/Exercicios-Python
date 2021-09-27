salario = float(input('\nDigite o seu salário: '))
if salario <= 1250:
    aumento = 15/100*salario
    print('Você terá um aumento de 15%. \nSalário atual: \33[1;33mR${:.2f}\33[m ' .format(salario+aumento))
else:
    aumento = 10/100*salario
    print('Você terá um aumento de 10%. \nSalário atual: \33[1;33mR${:.2f}\33[m '.format(salario+aumento))
print('-'*50)
