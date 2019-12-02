from random import randint
dados ={}
for i in range(0,4):
    dados['jogador'] = i+1
    dados['dado'] = randint(1,6)
print(dados)
