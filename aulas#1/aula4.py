# atividade 31
vel = int(input('Qual é a velocidade atual do carro? '))

if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você exedeu o limite permitido que é de 80KM/H')
    print('Você deve pagar uma multa de R$280.00!')
    
    print('Tenha um bom dia! Dirija com segurança!')

# atividade 32
num = int(input('me diga um número qualquer: '))
result = num % 2

if result == 0:
    print('o resultado foi {} e ele é par'.format(num))
else:
    print('o resultado foi {} e ele é ímpar'.format(num))

# atividade 33
dis = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))

pre1 = (0.50 * dis)
pre2 = (0.45 * dis)

if dis <= 200:
    print('E o preço da sua passagem será de R${}'.format(pre1))
else:
    print('E o preço da sua passagem será de R${}'.format(pre2))

# atividade 34
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

# atividade 35
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
p3 = int(input('Terceiro valor: '))

meno = p1
if p2<p1 and p2<p3:
    menor = p2
if p3<p1 and p3<p2:
    menor = p3

maior = p1
if p2>p1 and p2>p3:
    maior = p2
if p3>p1 and p3>p2:
    maior = p3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

# atividade 36
