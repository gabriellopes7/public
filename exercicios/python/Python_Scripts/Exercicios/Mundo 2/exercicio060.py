n = int(input('Digite um numero: '))
f = 1
resultado = 1
while f<=n:
    resultado *= f
    f+=1
print('O fatorial de {} é {}'.format(n,resultado))