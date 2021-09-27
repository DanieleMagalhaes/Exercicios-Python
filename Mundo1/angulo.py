#math.cos(numero): Retorna o cosseno do número em radiano.
#math.sin(numero): Retorna o seno do número em radiano.
#math.tan(numero): Retorna a tangente do número em radiano.
#math.radians(numero): Converte o angulo ‘numero’ de graus para radiano.

from math import cos, sin, tan, radians 
print('\nCALCULO DA SEN, COS E TAN DE UM ANGULO. \n')
angulo = int(input('Digite o valor do ângulo '))
radiando = radians(angulo)
print('SENO: {:.2f} ' .format(sin(radiando)))
print('COSSENO: {:.2f}' .format(cos(radiando)))
print('TANGENTE: {:.2f} \n' .format(tan(radiando)))
