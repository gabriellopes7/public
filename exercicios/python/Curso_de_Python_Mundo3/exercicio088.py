from random import randint
from time import sleep

jogo =[]
listaJogos=[]


tot=0
print('-'*50)
n = int(input('Digite a quantidade de jogos desejada: '))
print('-'*50)
while tot<n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont+=1
        if cont>=6:
            break
    jogo.sort()
    print(f'Jogo {tot+1}: {jogo}')
    sleep(1)
    listaJogos.append(jogo[:])
    jogo.clear()
    tot+=1
for p,j in enumerate(listaJogos):
    print(f'Jogo {p+1}: {j}')
    sleep(1)


