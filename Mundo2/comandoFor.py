for f in range(6, 0, -1): #conta para traz
    print(f)
print('FIM')

print('-'*60)
numero = int(input('\nDigite um número: '))
for c in range (1,numero+1): #ultimo não considera por isso soma 1
    print(c, end=' ')
print('FIM')

print('-'*60)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Pulando: '))
for x in range (i, f+1, p): #começa em i, termina em f contando de p em p. 
    print(x, end=' ')
print('FIM')


print('-'*60)
s = 0
for y in range (0,4): #0, 1, 2, 3 - ultimo não considera
    n = int(input('Digite um valor: '))
    s = s + n #OU s +=n
print('A soma desses valores é: {}' .format(s))