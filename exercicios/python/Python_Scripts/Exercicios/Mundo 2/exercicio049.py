n = int(input('Digite um numero de 1 a 9: '))
for c in range(0,11):
    print('{:2} x {:2} = {:2}'.format(n,c,n*c))