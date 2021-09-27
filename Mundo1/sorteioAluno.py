#Um professor quer sortear um de seus 4 alunos para apagar o quadro. Crie um programa que ajude-o, lendo o nome deles e escrevendo o nome do escolhido na tela.
from random import choice
a1 = str(input('\nDigite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4 ]
print('\nO aluno sorteado foi: {}' .format(choice(alunos)))