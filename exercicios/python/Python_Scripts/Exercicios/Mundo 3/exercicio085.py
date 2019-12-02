valores =[]
pares=[]
impares=[]
for n in range(0,7):
    num = int(input('Digite um número: '))
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
valores.append(pares)
valores.append(impares)
print(valores)