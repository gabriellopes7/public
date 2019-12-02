num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7) #insere um elemento na ultima posição
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,0)
print(num)
print(len(num))
num.pop() #remove o ultimo valor
print(num)
num.pop(2) #remove o elemento da posição 2
print(num)
num.remove(2) #remove o elemento de VALOR 2
print(num)
num.insert(2,2)
num.append(2)
print(num)
num.remove(2) #vai remover somente o elemento de valor 2 da lista
print(num)
num.insert(2,2)
num.append(2)
num.append(2)
print(num)
#para remover todos os elementos de mesmo valor de uma lista
for item in num:
    num.remove(2)
print(num)
