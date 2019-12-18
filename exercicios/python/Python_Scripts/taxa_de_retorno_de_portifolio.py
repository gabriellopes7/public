import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

#carteira Monetus
tickers = ['BIDI11.SA','HGTX3.SA','EZTC3.SA','HAPV3.SA','CVCB3.SA','RAPT4.SA','GRND3.SA','ABCB4.SA','MDIA3.SA','POMO4.SA','POMO3.SA','CGRA3.SA']
mydata = pd.DataFrame()

print(mydata.tail())
#mydata = wb.DataReader('NATU3.SA',data_source='yahoo',start='1995-1-1')['Adj Close']
#print(mydata)

#inserindo a coluna ADJ Close de todos os dados em uma tabela de index data
for t in tickers:
    mydata[t] = wb.DataReader(t,data_source='yahoo',start='2016-1-1')['Adj Close']
print(mydata)
mydata.info()
#(mydata/mydata.loc['2019-1-2']*100).plot(figsize=(15,6))
#plt.show()

#me mostra os dados do index referente
#print(mydata.loc['2019-1-2'])
#me mostra os dados da linha mostrada, posição de interesse
#print(mydata.iloc[0])

#calculando o retorno dos investimentos
returns = (mydata/mydata.shift(1))-1
returns.head()

#pesos das ações
pesos = (0.1743,0.1354,0.1517,0.12,0.0776,0.0505,0.0525,0.0363,0.0215,0.0219,0.0110,0.0012)

#método do numpy para multiplicação de matrizes np.dot
np.dot(returns, pesos)

#calculando retorno anual
annual_returns = returns.mean()*250
print(annual_returns)

#multiplicando matrizes
np.dot(annual_returns,pesos)

print(f'{np.dot(annual_returns,pesos)*100:.2f}' + '%')
