# an = a1 + (n - 1) * r    → enésimo termo da pa

# an : termo que queremos calcular
# a1: primeiro termo da P.A.
# n: posição do termo que queremos descobrir
# r: razão

print('='*40)
print('10 TERMOS DE UMA PA')
print('='*40)
a1 = int(input('Digite a 1º termo da P.A.: '))
r = int(input('Digite a razão: '))
an = a1 + (10 - 1) * r
for pa in range (a1, an + r, r): # + r pq ele faz 9 termos e somando mais a razao add o ultimo
    print('{}'.format(pa), end=" → ")
print('fim')