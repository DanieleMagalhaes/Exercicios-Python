from time import sleep
sleep(1)
print('\n\33[32mVamos para a contagem regressiva:\33[m \n')
sleep(2)
for c in range(10, 0 , -1):
    print(c, end='  ')
    sleep(1)
print('\n\33[33mFeliz ANO NOVO!!! \33[m\n')