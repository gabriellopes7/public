import numpy as np 

arr = np.arange(0,30,3)
print(arr)

#pode-se puxar os valores através do índice
print(arr[3])#puxando o 9

#indice inicial e final
print(arr[2:5])#puxa 2,3,4 não puxa o 5

#puxando elementos até um certo índice
print(arr[:5]) #puxa todos até o 5
 
#puxando elementos A PARTIR de um índice
print(arr[1:]) #puxa do 1 pra frente

#alterando vários valores no array
arr[3:] = 100
print(arr)

#arrays bidimensionais
arr = np.arange(50).reshape(5,10) #criando um array de 50 números e colocando ele no formado de 5x10
print(arr)
print(arr.shape)

print(arr[:4][:]) #para ver os elementos até a linha 3, todos os elementos

print(arr[:,3]) #para ver todos os elementos de todas as linhas e apenas de uma coluna


#apontamento de arrays
#um array referenciado em outro array, gera alteração mútua entre eles
arr2 = arr[:3] #estou jogando o array 2 com todos os elementos até a terceira linha do primeiro array
arr2[:] = 100 #alterei todos os elementos de arr2 para 100
print(arr) #mostrando que o array 1 foi alterado

#para não causar alteração no array inicial, deve-se usar o método copy
arr = np.arange(50).reshape(5,10)
arr2=arr[:3].copy()
arr2[:2] = 100
print(arr)
print(arr2)
#neste caso apenas o arr2 foi alterado

#fatiando arrays
#encontrar elementos entre as linhas de 1 a 3, da coluna 5 em diante
print(arr[1:4,5:])

#fazendo slice com um dado boleando
bol = arr>15
print(bol) #cria uma matriz de booleans para comparativo
#o shape do array de booleanos tem que ser igual ao que vc está comparando
print(arr[bol]) #imprime somente os valores onde os valores são true

#para puxar elemento específico
array = np.linspace(0,100,30)
print(array)
print(array.shape)
array = array.reshape(3,10)
print(array)#aqui ele se tornou uma matriz de 3x10
#desejo retirar os elementos até a linha de indice 1 e da coluna 2
print(array[:2,2])