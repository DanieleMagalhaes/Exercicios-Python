print('='*30)
print(' '*5, ' BOLETIM ', ' '*5)
print('='*30)
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
    print('='*30)
print()
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>10}') # < alinhado a esquerda > a direita
print('-'*30)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')
while True:
    print('-'*30)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('\nFINALIZANDO...')
        break
    if opcao <= len(ficha) - 1: # -1 pq começa no 0 e o ultimo é n-1
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<'*5, ' VOLTE SEMPRE! ', '>'*5)