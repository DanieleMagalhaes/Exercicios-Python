#Um professor quer sortear a ordem de apresentação de um trabalho de 4 alunos. Crie que o nome deles e escrevendo q ordem de apresentação de cada aluno.
from random import shuffle
a1 = str(input('\nDigite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4 ]
shuffle(alunos)
print('\nA ordem de apresentação do alunos é: \n {}' .format(alunos))

