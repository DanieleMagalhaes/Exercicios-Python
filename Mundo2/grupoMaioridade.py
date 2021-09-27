from datetime import date
atual = date.today().year
print('='*70)
maior = 0
menor = 0
for p in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos \33[32m{} pessoa(s) maiores de idade\33[m\nE \33[33m{} pessoa(s) menores de idade\33[m.'.format(maior,menor))
print('='*70)

