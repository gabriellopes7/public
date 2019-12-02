import random
n = random.randint(0,5)
escolha = int(input('Tente adivinha um número de 0 a 5: '))
if escolha == n:
    print('Parabéns, você acertou, o número sorteado era {}'.format(n))
else:
    print('Você errou, o número sorteado era {}'.format(n))

