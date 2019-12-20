import numpy as np 
#serve para trabalhar com álgebra linear

minha_lista=[1,2,3]
print(minha_lista)
print(np.array(minha_lista))
#converte a lista em um array numpy

#matriz em numpy
minha_matriz = [[1,2,3],[4,5,6],[7,8,9]] 
#conte a quantidade dos primeiros colchetes, para saber a dimensão da matriz
print(np.array(minha_matriz))

#metodo arange, cria sequencia de números (inicio, final,passo[opcional])
print(np.arange(0,10)) #exclui o 10, ultimo elemento nunca está incluso
print(np.arange(0,11,2)) #arange com passos 2, o step padrão é 1

#array de zeros
print(np.zeros(3))

#matriz de zeros
print(np.zeros((5,5)))

#array de uns
print(np.ones(5))

#matriz de ones(uns)
print(np.ones((5,5)))

#matriz identidade(1 na diagona e 0 nos outros dados)
print(np.eye(4)) #cria uma matriz identidade 4x4

#linspace, semelhante ao arrange, especifica inicio, fim e quantos números
#você deseja ver no intervalo dessa série
print(np.linspace(0,10,100))

#criação de matrizes e arrays aleatórios
print(np.random.rand(5)) #cria 5 números aleatórios entre 0 e 1
#para criar de 0 a 100 é so multiplicar por 100

#criação de matriz multidimensional não precisa informar uma tupla, apenas um parâmetro a mais
print(np.random.rand(5,5))

#randn -> retorna numeros aleatorios que não são tirados de uma distribuição uniforme
print(np.random.randn(4))

#randint-> (inicio, fim, quantidade de numeros), retorna uma quantidade de numeros inteiros dentro
#de um intervalo
print(np.random.randint(0,100,10))
#para se obter o mesmo resultado usando rand
print(np.round(np.random.rand(4)*100,0))


#reshape -> alterando formado do array
arr = np.random.randn(25)
print(arr)
arr = arr.reshape(5,5)
print(arr) #aqui ele vira uma tupla

#PARAMETRO
#acessando a característica do objeto
print(arr.shape) #para ver as dimensões do objeto

#trazendo maior valor e menor
print(arr.max())
print(arr.min())

#para retornar o índice em que o maior/menor elemento se encontra
print(arr.argmax())
print(arr.argmin())