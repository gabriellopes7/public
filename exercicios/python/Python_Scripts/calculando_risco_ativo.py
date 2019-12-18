import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

tickers = ['PG','BEI.DE']
sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t]=wb.DataReader(t,data_source='yahoo',start='2007-1-1')['Adj Close']
print(sec_data.tail())

#retornos logaritmicos
sec_returns = np.log(sec_data/sec_data.shift(1))-1
print(sec_returns)

#Calculo para o risco da PG
print(sec_returns['PG'].std()*250**0.5) #std() -> standard deviation = desvio padrão
#para variância é só retirar 0.5 da formula
print(sec_returns['PG'].std()*250)

#comparando os riscos das duas empresas
print(sec_returns[['PG','BEI.DE']].std()*250**0.5) #desvio padrão
print(sec_returns['PG'].var()*250) #calculo da variância
print(sec_returns.cov()) #calculo da covariância anual
print(sec_returns.corr()) #calculo da correlação