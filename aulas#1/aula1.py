# atividade 1
nome = input('qual é o sue nome?')
print('olá', nome, 'é um prazer lhe conhecer')

# atividade 2
dia = input('em que dia você nasceu?')
mes = input('em que mes você nasceu?')
ano = input('em que ano você nasceu?')

print('então', nome, 'você nasceu em:', dia,'/',mes,'/',ano,'?')

# atividade 3
numero_1 = input('digite um número')
numero_2 = input('digite um número')

print(int(numero_1) + int(numero_2))

# atividade 3   
print('hello world')    

# atividade 4
nome2 = input('qual é o seu nome?')
print('é um prazer lhe conhecer, {}!'.format(nome2))  

# tipos primitivos no python e as peculiaridades do:
# int(números inteiros) / float(números reais) / bool(True or False) / str(textos com 'isso')

# atividade 5
n1 = int(input('digite um número'))
n2 = int(input('digite outro número'))
r = n1 + n2

print('a soma entre {} e {} vale {}!'.format(n1,n2,r))

# atividade 6
texto = input('digite algo: ')

print('o tipo primitivo desse valor é:', type(texto))

print('só tem espaços? ', texto.isspace())
print('é um número? ', texto.isnumeric())
print('é alfabético? ', texto.isalpha())
print('é alfanumério? ', texto.isalnum())   
print('está em maiúsculas ', texto.isupper())
print('está em minúsculas? ', texto.islower())
print('está capitalizado? ', texto.istitle())

# atividade 7
n = int(input('digite um número: '))
s = n + 1
an = n - 1

print('analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n,an,s))

# atividade 8
import math

n = int(input('digite um número: '))
dob = n * 2
tri = n * 3
rai = math.sqrt(n)

print('o dobro de {} vale {}.'.format(n,dob))
print('o triplo de {} vale {}.'.format(n,tri))
print('a raiz quadrada de {} é igual a {}.'.format(n,rai))

# atividade 9
nota1 = int(input('primeira nota do aluno: '))
nota2 = int(input('segunda nota do aluno: '))
media = int(nota1 + nota2) / 2

print('a média entre {} e {} é igual a {}'.format(nota1,nota2,media))

# atividade 10
metros = float(input('digite uma distância em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('a medida de {} corresponde a '.format(metros))

print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))