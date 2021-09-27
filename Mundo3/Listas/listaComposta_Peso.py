cadastro = []
dado = []
maior = menor = 0
print('='*60)
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    cadastro.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-'*40)
    if resp in 'N':
        break
print('='*60)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'O mais leve tem {menor}kg. Peso de: ', end='')
for c in cadastro:
    if c[1] == menor:
        print(f'[{c[0]}]', end=' ')
print(f'\nO mais pesado tem {maior}kg. Peso de: ' , end='')
for c in cadastro:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')
