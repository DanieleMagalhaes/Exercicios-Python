# ATIVIDADES DA SEMANA 4 - UNIVESP
#EXE1
print('\n\33[1;33mSEMANA 4\33[m')
print('\33[1;32mEXE 1:\33[m')
a = 'olá'
b = 'classe'
res = a + ' ' + b + ', ' + a + ' ' + a
print(res)

#EXE2
print('\n\33[1;32mEXE 2:\33[m')
l = [1, 2, 3]
l[l[1]] = 5   # l[ l[1] = 2  (indice = 1)] = 3 (indice 2) vai trocar pelo 5
print(l)

#EXE3
print('\n\33[1;32mEXE 3:\33[m')
t = 4
t = t/4     # (4/4=1)
t = 2 > 2   # 1 > 2 = False
print(t)

# ATIVIDADES DA SEMANA 5 - UNIVESP
#EXE1
print('\n\33[1;33mSEMANA 5\33[m')
print('\33[1;32mEXE 1:\33[m')
var = input('Digite um número: ')
if var == 5:
    print('a')
if var == 4:
    print('b')
else:
    print('c')

#EXE2
print('\n\33[1;32mEXE 2:\33[m')
x = 3
y = 2
if x % y < x:           # Se (3%2)= 1 < 3           >> TRUE
    if y * 10 >= x/3:   # Se (2*10)=20 >= (3/3)=1   >> TRUE  
        print('a')      # Imprime a
    print('b')          # Imprime b
else:
    print('c')          # Senão >> FALSE >> Não imprime 
print('d')              # Fim >> Imprime d

#EXE3
print('\n\33[1;32mEXE 3:\33[m')
x = 5
y = 4
if x * y >= x / y:      # Se (4*5)=20 >= (5/4)=1,25 >> TRUE
    if y % 2 != 1:      # Se (4%2)=0 != 1           >> TRUE
        print('a')      #Imprime a
        print('b')      #imprime b
else:                   # Senão >> FALSE
    print('c')          # Não imprime 
print('d')              # Imprime d

#EXE4
print('\n\33[1;32mEXE 4:\33[m')
a = [1,2,3]
b = a           # b = [1,2,3]
b[1] = 4        # b = [1,4,3] logo a = [1,4,3]
print(f'a = {a}')
print(f'b = {b}')
if a == b:      # TRUE
    print('a')  # Imprime a 
else:           # FALSE
    print('b')  # Não imprime
a = (4,5,6)   
b[1] = 7        # b = [1,7,3]
print(f'\na = {a}')
print(f'b = {b}')
if a == b:      # FALSE
    print('c')  # Não imprime
else:           # TRUE
    print('d')  # Imprime d

#EXE 5
print('\n\33[1;32mEXE 5:\33[m')
str1 = 'abc'
str2 = 'acbd'
if str1 < str2: #True >> Imprime a 
    print('a')
else:
    print('b')
if len(2 * str1) > len(str2): # Se tamanho(2*abc)= 6 > tamanho(4)  >> TRUE  >> Imprime c
    print(f'Tamanho de str1: {len(2 * str1)}')
    print(f'Tamanho de str2: {len(str2)}')
    print('c')
else:
    print('d')

resp = str(input('Digite uma letra: '))
if resp[0] in 'aeiou':
    print(f'{resp} começa com a vogal!')
else:
    print('Não começa com vogal!')
