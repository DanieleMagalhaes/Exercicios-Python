# exercicio 83 - Validando expressão matemática
print('-'*60)
expressao = str(input('Digite uma expressão matemática: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo ==')':
        if len(pilha) > 0: #se pilha não estiver vazia
            pilha.pop()    #remove ultimo elemento
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão errada! Faltou parênteses')
print('-'*60)
