import numpy as np 
import matplotlib.pyplot as plt 

x=np.linspace(0,10,10)
y=x**2
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x,x**2,'r') #pode-se usar o parametro color='string' '#rgb'
ax.plot(x,x**3,'b--')
ax.plot(x,x/2,color='#FF008B',linewidth='2',alpha=0.5) #linewidth ou lw= grossura da linha, alpha=transparencia em %
ax.plot(x,x/3,color='black',lw='3',linestyle='-.') #linestyle=estilo da linha
plt.show()

#opções de gráficos
##################
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# Possiveis estilos de linha: ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# Traços estilizados
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # Formato: comprimento da linha, comprimento do espaço, ...

# possíveis símbolos de marcador: marcador = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# tamanho e cor do marcador
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
plt.show()

#--------------------------------------#
#definindo limites para o gráfico
fig,ax=plt.subplots()
ax.plot(x,x**2)
ax.set_xlim([0,100]) #limite de X
ax.set_ylim([0,100]) #limite eixo Y
plt.show()

#tipos especiais de plotagem
###############

plt.scatter(x,y)
plt.show()

from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# box plot retangular
plt.boxplot(data,vert=True,patch_artist=True)
plt.show()

#tutorial da biblioteca http://www.loria.fr/~rougier/teaching/matplotlib