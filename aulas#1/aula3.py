# atividade 21
'''
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
'''
# atividade 23
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('"C:\Users\angab\Desktop\Mogolovonio.mp3"')
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()