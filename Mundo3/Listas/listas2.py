print('='*60)
pessoa = list()
pessoa.append('Daniele')
pessoa.append(33)
print(f'Pessoa: {pessoa}')
galera = list()
galera.append(pessoa[:]) #copia de pessoa
print(f'Galera: {galera}')
pessoa[0] = 'Maria'
pessoa[1] = 22
galera.append(pessoa[:])
print(f'Galera: {galera}')
print('='*60)

pessoal = [['João', 19], ['Ana', 25], ['Pedro', 14], ['Cristina', 33]]
print(pessoal[0])
print(pessoal[0][0])
print(pessoal[2][1])
print('='*60)
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('='*60)

cadastro = []
dado = []
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    dado.append(str(input('Profissão: ')))
    print('-'*40)
    cadastro.append(dado[:])
    dado.clear()
for c in cadastro:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade!')
        maior +=1
    else:
        print(f'{c[0]} NÃO é maior de idade! ')
        menor +=1
print(cadastro)
print(f'Temos {maior} maior(es) e {menor} menor(es) de idade.')
