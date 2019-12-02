import random
n = random.randint(0,5)
escolha = -1
c=0
while escolha != n:
    escolha = int(input('Tente adivinha um número de 0 a 5: '))
    if escolha != n:
        print('Você errou, tente de novo!')
    c+=1
print('Parabéns, você acertou, o número sorteado era {}'.format(n))
print('Você tentou {} vezes'.format(c))

