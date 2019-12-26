import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use('ggplot')
df3 = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Visualização de dados incorporada do Pandas\df3')
print(df3.head())

#grafico de dispersao de bxa
df3.plot.scatter(x='b',y='a',s=50,c='red',figsize=(12,3))
plt.show()

#histograma da coluna a
df3['a'].plot.hist()
plt.show()

#adicionando mais barras
df3['a'].plot.hist(alpha=0.5,bins=25)
plt.show()

#boxplot comparando a com b
df3[['a','b']].plot.box()
plt.show()

#plot kde da coluna d
df3['d'].plot.kde()
plt.show()

#aumentando largura da linha e colocando pontilhado
df3['d'].plot.kde(lw=3,ls='--')
plt.show()

#outra resposta
df3['d'].plot.density(lw=5,ls='--')
plt.show()

#Crie um gráfico de área de todas as colunas para apenas as linhas até 30. (sugestão: use .ix). **
df3.ix[0:30].plot.area(alpha=0.4)
plt.show()