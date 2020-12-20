from random import shuffle
num1 = str(input('Primeiro aluno: -> '))
num2 = str(input('Segundo Aluno: -> '))
num3 = str(input('Terceiro aluno: -> '))
num4 = str(input('Quarto aluno: -> '))
num5 = str(input('Quinto aluno: -> '))
lista = [num1, num2, num3, num4, num5]
shuffle(lista)
print('A ordem de apresentação sera? ')
print(lista)
