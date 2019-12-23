import numpy as np 

#Crie uma matriz de 10 zeros
arr = np.zeros(10)
print(arr)

#### Crie uma matriz de 10 ones
arr = np.ones(10)
print(arr)

#### Crie uma matriz de 10 cincos
arr = np.ones(10)*5
print(arr)

#Crie um array de inteiros de 10 até 50
arr = np.arange(10,51)
print(arr)

#### Crie um array dos numeros pares de 10 até 50
arr = np.arange(10,51,2)
print(arr)

#### Criei uma matriz 3x3 com valores variando de 0 até 8
arr = np.arange(0,9)
arr = arr.reshape(3,3)
print(arr)

#### Crie uma matriz identidade 3x3
arr = np.eye(3)
print(arr)

#### Use NumPy para gerar números aleatórios entre 0 e 1
arr = np.random.rand(1)
print(arr)

#Use Numpy para gerar um array de 25 números aleatórios tirados de uma distribuição normal.
arr = np.random.randn(25)
print(arr)

#crie a matriz de 0 a 1
arr = np.linspace(0.01,1,100)
arr = arr.reshape(10,10)
print(arr)

#Crie um array de tamanho 20 igualmente espaçado entre 0 e 1
arr = np.linspace(0,1,20)
print(arr)

#matrizes conforme output
mat = np.arange(1,26).reshape(5,5)
print(mat)

# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
print(mat[2:,1:])

#20
print(mat[3,4])

# array([[ 2],
#        [ 7],
#        [12]])
print(mat[:3,1])

#array([21, 22, 23, 24, 25])
arr = mat[4]
print(arr)

# #array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
print(mat[3:])

#### Obter a soma de todos os valores no "mat"
print(mat.sum())

#### Obter o desvio padrão dos valores em mat
print(mat.std())

##### Obter a soma de todas as colunas em mat
print(mat.sum(axis=0))

##### Obter a soma de todas as linhas em mat
print(mat.sum(axis=1))