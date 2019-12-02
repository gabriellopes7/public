from random import choice
maquina = [1,2,3]
opcao = choice(maquina)
print('1-Tesoura\n2-Papel\n3-Pedra')
jogador = int(input('Digite a opcao desejada: '))
if opcao == 1:
    print('Maquina jogou Tesoura')
elif opcao == 2:
    print('Maquina jogou Papel')
else:
    print('Maquina jogou Pedra')
#jogo
if jogador == opcao:
    print('Empate')
elif ((jogador == 1 and opcao == 2) or (jogador == 2 and opcao ==3) or (jogador == 3 and opcao ==1)):
    print('Você ganhou !')
else:
    print('Você perdeu !')

