n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.3f}' .format(soma, sub, mult, div), end= ' ')
print('A divisão inteira é {} e a potência é {}' .format(divInt, exp))