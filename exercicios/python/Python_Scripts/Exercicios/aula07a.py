nome = input('Qual é o seu nome ?')
print('Prazer em te conhecer {}'.format(nome))
print('Prazer em te conhecer {:20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome))
print('Prazer em te conhecer {:=^20}'.format(nome))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {} e a exponenciação é {}'.format(s,m,d,di,e))
