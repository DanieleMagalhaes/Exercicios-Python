#exe Univesp ultilizando x = 4, mas fiz o usuário digitar o valor de x.
x = float(input('\nDigite um valor x: '))
h = (3/((1/(3.6+x)) + (1/(8.9+x)) + (1/(10+x))))-x
print('A resposta é: {:.3f}' .format(h))