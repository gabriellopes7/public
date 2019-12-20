#Matplot lib
#biblioteca de visualização de dados mais popular do python
#ela te da o controle sobre todos os aspectos da sua figura
#ela foi projetada para ter métodos de plotagem do Matlab

#para instalar
#pip install matplotlib

#matplotlib.org
#gallery -> te da várias instruções para construir os gráficos
import matplotlib.pyplot as plt 
import numpy as np 

#criando um espaço vetorial
x = np.linspace(0,5,11)
print(x)
y = x**2
print(y)

#Funcional
plt.plot(x,y) #não te deixa manipular muito os dados
plt.xlabel('Eixo X')
#nome do eixo X
plt.ylabel('Eixo Y')
#nome do eixo Y
plt.title('Gráfico 1')
#titulo do grafico
plt.show()
#mostrar o gráfico

#mudando a cor do gráfico
plt.plot(x,y,color='red')
plt.show()

#colocando o gráfico tracejado
plt.plot(x,y,'r--')
plt.show()

##

#Plot com 2 gráficos
#plt.subplot(nrows=1,ncols=2,element=1) #plota um gráfico com uma quantidade especifica de linhas e de colunas
#não é necessário informar nrows e ncols, sabe-se que a ordem já é essa, logo:
#plt.subplot(linhas,colunas,elemento que iremos trabalhar)
plt.subplot(1,2,1) #metodo mais simplista
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()

#subplotS() é o método orientado a objetos

#criando instancias de objetos
fig = plt.figure()
#cria uma figura vazia

#criando um eixo derivado de uma figura
axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) #([% de distancia da borda esquerda,%distancia da borda inferior,largura,altura])
axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
axes1.plot(x,y)
axes2.plot(y,x)
axes1.set_xlabel('Eixo X')
axes1.set_title('Título')
plt.show()

#Usando o subplots()
fig, ax = plt.subplots() #a função cria duas instâncias, figura = fig, e eixo = ax
#eixo unico
#ax recebe uma lista com todos os eixos da figura
ax.plot(x, x**3,'b--') #não é mais o plot do PLT é o plot do da instância de classe eixo
ax.plot(x,x**4,'g-.')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Gráfico composto')
plt.show()

#fazendo gráficos multiplos com subplots
fig2, ax2 = plt.subplots(1,2)
for i,a in enumerate(ax2):
    a.plot(x*(i+1),y*(i+1))
    a.set_title(f'Gráfico {i+1}')
plt.show()
#ou pode-se usar o número do elemento
fig3,ax3=plt.subplots(1,2)
ax3[0].plot(x,y)
ax3[1].plot(y,x)
plt.show()


fig,ax = plt.subplots(5,5) #cria 25 gráficos
plt.tight_layout() #organiza o layout dos gráficos para ficar mais visual

#modificando os atributos da digura
fig, ax = plt.subplots(1,1,figsize=(12,3),dpi=100) #figsize=(largura,altura) dpi=resolução
ax.plot(x,y,'r--')
plt.show()

#salvando o último gráfico (suporta png, gif, pdf, eps,raw, rgba)
fig.savefig(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Matplotlib\fig1.png')

#inserindo legenda
fig, ax = plt.subplots(1,1)
ax.plot(x,y,label='x^2')
ax.legend(loc=0) #loc=(1-superior direito, 2-superior esquerdo,0=automatico)
plt.show()