print('='*60)
filme = {'titulo': 'Star Wars',
            'ano': 1977,
            'diretor': 'George Lucas',
            'gênero': 'Ficção Científica'}
print(filme)
print(filme['titulo'])
print(f'\nO filme é {filme["titulo"]} de {filme["ano"]}.')
print(filme.values())
print(filme.keys())
print(filme.items())
del filme['diretor'] #deleta campo
print()

#imprime as chaves
for k in filme.keys():
    print(f'{k}')
print()

#imprime os valores
for v in filme.values():
    print(f'{v}')
print()

#imprime as chaves e valores
for k, v in filme.items():
    print(f'O {k} é {v}')
print('='*60)

# DICIONARIOS DENTRO DE LISTAS

brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
estado3 = {'uf':'Minas Gerais', 'sigla':'MG'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(estado1)
print(brasil)
print(brasil[1])
print(brasil[2]['uf'])
print('='*60)

mundo = list()
país = dict()
#Receber dados
for c in range(0, 3):
    país['nome'] = str(input('País: '))
    país['idioma'] = str(input('Idioma: '))
    print('-'*40)
    mundo.append(país.copy()) #metodo fazendo copia
#Imprimir dados
for p in mundo:
    print(p)
print()
#imprimin dados
for p in mundo: #for da lista
    for k, v in p.items(): #for do dicionario
        print(f'O campo {k} tem valor {v}.')
