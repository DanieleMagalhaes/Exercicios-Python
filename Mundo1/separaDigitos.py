#usando string
numero = str(input('\nDigite um número de 0 a 9999: '))
print('Unidade: {} '.format(numero[3]))
print('Dezena: {} ' .format(numero[2]))
print('Centena: {} ' .format(numero[1]))
print('Milhar: {} ' .format(numero[0]))

# matematica
numero = int(input('\nDigite outro número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {} '.format(u))
print('Dezena: {} ' .format(d))
print('Centena: {} ' .format(c))
print('Milhar: {} ' .format(m))