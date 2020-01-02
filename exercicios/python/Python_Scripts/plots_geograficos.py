#plots geográficos são desafiadores, devido a gama de formatos que se 
# é possível construí-los
# o matplotlib tem uma extensão chamada de basemap que permite esse tipo de plotagem 
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import chart_studio.plotly as py 
#pre instrução para trabalhar no modo offline
init_notebook_mode(connected=True)

import pandas as pd 
data = dict(type='choropleth', locations=['AZ','CA','NY'], locationmode='USA-states',colorscale='Portland',text=['Texto1','Texto2','Texto3'],z=[1.0,2.0,3.0],colorbar={'title':'Titulo da barra de cores'})
layout = dict(geo={'scope':'usa'})
choromap=go.Figure(data=[data],layout=layout)
plot(choromap)

df = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Geographical Plotting\2011_US_AGRI_Exports')
print(df.head())

#mapa dos estados unidos de producao agricola
data=dict(type='choropleth',colorscale='ylorrd',locations=df['code'],z=df['total exports'],locationmode='USA-states',text=df['text'],colorbar={'title':'Milhoes de Dólares'})
layout=dict(title='Exportações agrícolas de 2011 por estado',geo=dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))
choromap = go.Figure(data=[data],layout=layout)
plot(choromap)