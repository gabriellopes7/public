import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

plt.style.use('ggplot') #alterando o estilo dos gráficos
#na biblioteca do matplotlib vc consegue ver os outros estilos que existem
df1 = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Visualização de dados incorporada do Pandas\df1',index_col=0)
print(df1.head())
df2=pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Visualização de dados incorporada do Pandas\df2')
print(df2.head())


#mostrando o histograma do pandas
df1['A'].hist()
plt.show()

#grafico de area
df2.plot.area(alpha=0.4)
plt.show()

#gráfico de barras
df2['a'].plot.bar()
plt.show()

#gráfico de barras empilhadas
df2.plot.bar(stacked=True)
plt.show()

#mostrando a frequencia no histograma
df1['A'].plot.hist() #pode-se usar bins
plt.show()

#gráfico de linhas
#df1.plot.line(x=df1.index,y='B') #deu erro
#possivel solucao, dar um nome para a coluna index e usá-la
#plt.show()

#scatter plot
df1.plot.scatter(x='A',y='B',c='C',cmap='inferno')
plt.show()
#podemos usar mais duas variáveis 
#c -> c define as cores dos pontos
#s -> s define os tamanhos dos pontos em função de outra variável
df1.plot.scatter(x='A',y='B',s=df1['C']*20)
#cmap -> paletta de cores
plt.show()


#boxplot
df1.plot.box()
plt.show()


#plot hexagonal
#criando um terceiro dataframe
df = pd.DataFrame(np.random.rand(1000,2),columns=['A','B'])
df.plot.hexbin(x='A',y='B',gridsize=20) #mudando o tamanho do grid com gridsize
#pode-se usar o cmap para alterar a paleta de cores
plt.show()

#plot de KDE
df2['a'].plot.kde() #é possivel mostrar o KDE de todos os dados
plt.show()