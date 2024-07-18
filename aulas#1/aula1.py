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