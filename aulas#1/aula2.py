# atividade 11
tabuada = int(input('digite um número para ver sua tabuada: '))

t1 = int(tabuada * 1)
t2 = int(tabuada * 2)
t3 = int(tabuada * 3)
t4 = int(tabuada * 4)
t5 = int(tabuada * 5)
t6 = int(tabuada * 6)
t7 = int(tabuada * 7)
t8 = int(tabuada * 8)
t9 = int(tabuada * 9)
t10 = int(tabuada * 10)

print('_____________')
print('                    ')
print('{}  x  1 = {}'.format(tabuada,t1))
print('{}  x  2 = {}'.format(tabuada,t2))
print('{}  x  3 = {}'.format(tabuada,t3))
print('{}  x  4 = {}'.format(tabuada,t4))
print('{}  x  5 = {}'.format(tabuada,t5))
print('{}  x  6 = {}'.format(tabuada,t6))
print('{}  x  7 = {}'.format(tabuada,t7))
print('{}  x  8 = {}'.format(tabuada,t8))
print('{}  x  9 = {}'.format(tabuada,t9))
print('{}  x  10 = {}'.format(tabuada,t10))

print('_____________')

# atividade 12
dinheiro = float(input('quanto dinheiro você tem na carteira? R$'))
dolar = float(dinheiro / 5)

print('com R${} você pode comprar US${}'.format(dinheiro,dolar))

# atividade 13
largurap = float(input('largura da parde: '))
alturap = float(input('altura da parde: '))

area = float(largurap * alturap)
litros = float(area / 2)

print('sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largurap,alturap,area))
print('para pintar essa parede, você precisará de {}L de tinta.'.format(litros))

# atividade 14
pre = float(input('qual é o preço do produto? R$'))
des = float(pre - (pre * 5 / 100))

print('o produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(pre,des))

# atividade 15
