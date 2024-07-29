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