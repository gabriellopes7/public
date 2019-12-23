import numpy as np 


#criando um array de 0 a 15 com passo 1
arr = np.arange(0,16)
print(arr)

#soma elemento indice por índice (elemento 0 + elemento 0) e devem ter o mesmo tamanho
print(arr + arr)

print(arr-arr)
print(arr/arr) #ela me dá um aviso, que encontrou uma divisão incorreta, mas devolveu uma reposta
#e onde está este erro ele me retorna NaN, que foi onde houve a divisão por 0
print(arr*arr)

print(1/arr) #neste caso, onde há a divisão por 0 retorna infinito

print(arr+100) #faz a operação índice por índice, aplicado em todos os elementos do array
print(arr*100)

#funções embutidas no numpy
##########
print(np.sqrt(arr)) #raiz quadradad do array
print(np.exp(arr)) #exponenciação
print(np.mean(arr)) #média (mean)
print(np.std(arr)) #desvio padrão (standard deviation)
print(np.sin(arr)) #seno dos elementos
print(np.max(arr)) #maior elemento do array
#ou
print(arr.max())
print(np.min(arr)) #menor elemento da lista
#ou
print(arr.min())

#https://docs.scipy.org/doc/numpy/reference/ufuncs.html  documentação


