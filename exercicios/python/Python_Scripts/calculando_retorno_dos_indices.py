import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

#tickers de indices de mercado
tickers = ['^GSPC', '^IXIC', '^GDAXI']
ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.DataReader(t,data_source='yahoo', start='1997-1-1')['Adj Close']
print(ind_data.head())

#colocando o grafico na base 100 e plotando
(ind_data/ind_data.iloc[0]*100).plot(figsize=(15,6))
plt.show()

ind_returns = (ind_data/ind_data.shift(1))-1
print(ind_returns.tail())

annual_ind_returns = ind_returns.mean()*250
print(annual_ind_returns)