import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt #coleção de funções de estilo distintas de matplotlib,
#para trabalhar com graficos e editar elementos
pg = wb.DataReader('PG', data_source='yahoo', start='1995-1-1') 
#importa dados da Procter & Gamble do Yahoo Finance
print(pg.head()) #mostra os 5 registros mais antigos
##instalar code runner extension
#pip install pandas_datareader
#pip install matplotlib.pyplot
#pip install numpy
print(pg.tail())##mostra os 5 registros mais recentes

#criando coluna de retorno
pg['simple return'] = (pg['Adj Close']/pg['Adj Close'].shift(1)) - 1
#shift -> pandas.DataFrame.shift(# de voltas) -> retorna uma quantidade de linhas
print(pg['simple return'])  

#PLOTANDO GRÁFICO

pg['simple return'].plot(figsize=(8,5)) #determina o tamanho do gráfico na área de resultado
plt.show() #mostra o gráfico

avg_returns_d = pg['simple return'].mean()
#pandas.DataFrame.mean() -> calcula a taxa média diária
print(avg_returns_d)

#para calcular a taxa média por ano, usamos mean()*250 -> que são os dias de negociação por ano
avg_returns_a = pg['simple return'].mean()*250
print(str(f'{avg_returns_a*100:.2f}') + '%') #transformando em string

#TAXA DE RETORNO LOGARITMICA
pg['log return'] = np.log(pg['Adj Close']/pg['Adj Close'].shift(1)) #para calcular o logaritmo de um número
print(pg['log return'])
pg['log return'].plot(figsize=(8,5))
plt.show()

log_return_d = pg['log return'].mean()
print(log_return_d)
log_return_a = pg['log   return'].mean()*250
print(str(f'{log_return_a*100:.2f}') + '%')