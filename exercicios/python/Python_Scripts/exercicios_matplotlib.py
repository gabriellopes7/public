import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
import matplotlib.pyplot as plt 


# #** Acompanhe estes passos: **

# ** Crie um objeto de figura chamado fig usando plt.figure () **
# ** Use add_axes para adicionar um eixo à tela de figura em [0,0,1,1]. Chame esse novo eixo de "ax". **
# ** Plote (x, y) nesses eixos e defina os rótulos e títulos para corresponder ao gráfico abaixo: **
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()

# ** Crie um objeto de figura e coloque dois eixos sobre ele, ax1 e ax2. 
# Localizado em [0,0,1,1] e [0,2,0,5, .2, .2], respectivamente. **
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
#** Agora plote (x, y) em ambos os eixos. E chame seu objeto de figura para mostrá-lo. **
ax1.plot(x,y)
ax2.plot(x,y)
plt.show()

#Crie o gráfico abaixo, adicionando dois eixos 
# a um objeto de figura em [0,0,1,1] e [0,2,0,5, .4, .4] 
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])
ax1.plot(x,z)
ax2.plot(x,y)
plt.show()

#Use plt.subplots (nrows = 1, ncols = 2) para criar o gráfico abaixo. **
fig3, ax3 = plt.subplots(nrows=1,ncols=2,figsize=(10,8))
ax3[0].plot(x,y,'--')
ax3[1].plot(x,z,'r')
plt.show()

#Veja se você pode redimensionar o gráfico adicionando o argumento figsize () em
#  plt.subplots () apenas copiando e colando seu código anterior.
fig3, ax3 = plt.subplots(nrows=1,ncols=2,figsize=(20,2))
ax3[0].plot(x,y, lw=3)
ax3[1].plot(x,z,'r')
plt.show()