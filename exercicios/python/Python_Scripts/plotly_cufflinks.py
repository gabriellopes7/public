#Plotly
#Biblioteca de dados interativa
#te da poder de interpretação dos dados
#precisa instalar antes de usar
#o plotly é uma empresa que armazena dados e visualizações
#tem interação com varios softwares, mysql, postgresql, excel,sqlserver
#permite criação de gráficos geográficos
#criação de gráficos financeiros
#interação com python, R e JavaScript
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from plotly import __version__
import plotly.graph_objs as go
import chart_studio.plotly as py
print(__version__)

#importando as classes que trabalham offline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot,plot
import cufflinks as cf
#conecta ao notebook
init_notebook_mode(connected=True)
#inicia o trabalho offline
cf.go_offline()

#criando um dataframe qualquer
df=pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df.head())

#criando um segundo dataframe
df2=pd.DataFrame({'Categoria':['A','B','C'],'Valores':[32,43,50]})
print(df2.head())

#gera um HTML para a visualização dos dados
#gráfico de marcadores
plot([go.Scatter(x=df['A'],y=df['B'],mode='markers')])
#https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf?_ga=2.263826444.1027275298.1577383106-871053511.1577383106

#gráfico de barras
plot([go.Bar(x=df2['Categoria'],y=df2['Valores'])])

#plotando todos os dados da base df
fig = go.Figure(data=go.Bar(y=df.count())) #como se eu tivesse feito um group by aqui
fig.write_html('first_figure.html', auto_open=True)

#boxplot
#não consegui
#para jupyter é assim \/
#df.iplot(kind='box')


#criando um terceiro dataframe
df3=pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,40,50],'z':[5,4,3,2,1]})
print(df3.head())
#plotando gráfico tridimensional
plot([go.Surface(colorscale='Viridis',z=df3)]) #colorscale é opcional

#gráfico spread
#só achei documentacao para jupyter
#df[['A','B']].iplot(kind='spread')

#histograma
plot([go.Histogram(x=df['A'])])
#no jupyter
#df['A'].iplot(kind='hist',bins=50)

#grafico de bolhas
plot([go.Scatter(x=df['A'],y=df['B'],marker=dict(color=['red','blue','green'],size=[30,80,200]),mode='markers')])
#no jupyter
#df.iplot(kind='bubble',x='A',y='B',size='C')

#matriz de dispersão
#no jupyter
#df.scatter_matrix()
