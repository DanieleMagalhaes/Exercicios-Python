times = ('Corinthians', 'Flamengo', 'São Paulo', 'Palmeiras', 'Santos', 'Vasco da Gama', 'Juventude', 
        'Fluminense', 'Grêmio', 'Esporte', 'Ceará', 'Internacional', 'Atlético-MG', 'Bahia', 'Botafogo',
        'Cruzeiro', 'Goiás', 'Chapecoence', 'Bragantino', 'Ponte Preta' )
print('='*60)
for t in range (0,len(times)):
    print('\33[34m{:2}º - {}\33[m'.format(t+1, times[t]))
print('='*60)
print(f'\33[32mOs 5 primeiros colocados são:\33[m {times[:5]}')
print(f'\33[32mOs 4 últimos colocados são:\33[m {times[-4:]}')
print(f'\33[32mTimes em ordem alfabética:\33[m {sorted(times)}')
print(f'\33[32mO Internacional está na \33[m {times.index("Internacional")+1}ª posição.')
    