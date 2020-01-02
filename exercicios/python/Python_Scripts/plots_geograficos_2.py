import numpy as np 
import pandas as pd 
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import chart_studio.plotly as py 
init_notebook_mode(connected=True)

#pibs dos países em 2014 em Bilhões
df = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\3. Python para Visualização de dados\Geographical Plotting\2014_World_GDP')
print(df.head())
data = dict(type='choropleth',locations=df['CODE'],z=df['GDP (BILLIONS)'],text=df['COUNTRY'],colorbar={'title':'PIB em Bilhões de Dólares'})
layout=dict(title='PIB mundo 2014',geo=dict(showframe=True,projection={'type':'mercator'}))
choromap= go.Figure(data=[data],layout=layout)
plot(choromap)
#link https://plot.ly/python/mapbox-county-choropleth/