# atividade 21
import random

auluno1 = str(input('primeiro aluno: '))
auluno2 = str(input('segundo aluno: '))
auluno3 = str(input('terceiro aluno: '))
auluno4 = str(input('quarto aluno: '))

lista = [auluno1,auluno2,auluno3,auluno4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

# atividade 22
import random

auluno1 = str(input('primeiro aluno: '))
auluno2 = str(input('segundo aluno: '))
auluno3 = str(input('terceiro aluno: '))
auluno4 = str(input('quarto aluno: '))

nomes = [auluno1,auluno2,auluno3,auluno4]

escolhido = random.shuffle(nomes)
print('a ordem apresentada será: ')
for nome in nomes:
    print(nome)

# atividade 23
import pygame

pygame.init()
pygame.mixer.music.load("Megalovania.mp3")
pygame.mixer.music.play()
pygame.event.wait()

'''
# operações com string's no python
-
frase = 'curso em vídeo python'
print(frase.strip[:21])
-
'''

# atividade 24
nome = str(input('digite seu nome completo: '))
print('analisando seu nome...')

nome_m = nome.upper()
nome_n = nome.lower()
nome_quantidade = len(nome.replace(' ', ' '))
separa = nome.split()

print('seu nome em maiúsculas é {}'.format(nome_m))
print('seu nome em minúsuculas é {}'.format(nome_n))
print('seu nome tem ao todo {}'.format(nome_quantidade))
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))