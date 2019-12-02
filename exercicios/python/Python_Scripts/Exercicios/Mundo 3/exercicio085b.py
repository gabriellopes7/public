valores =[[],[]]
for n in range(0,7):
    num = int(input('Digite um número: '))
    if num%2==0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(valores[0])
print(valores[1])