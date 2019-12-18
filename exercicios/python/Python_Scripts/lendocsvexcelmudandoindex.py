#Códigos para mudar indexação de dados Temporais

import pandas as pd
import numpy as np
mydata = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_para_financas\57 Importing Data - Part III\CSV\Python 3 CSV\Data_02.csv')
print(mydata.head())

##Colocando o index(indice) da tabela na coluna data
mydata = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_para_financas\57 Importing Data - Part III\CSV\Python 3 CSV\Data_02.csv', index_col='Date')
#index_col='Date'
print(mydata.head())
#Aqui a coluna date virou o índice

#Ler Excel
mydata2 = pd.read_excel(r'C:\Users\Gabriel Ladeira\Documents\python_para_financas\57 Importing Data - Part III\CSV\Python 3 CSV\Data_03.xlsx')
print(mydata2)
#Alterando o index para uma tabela excel, é necessário salvar o arquivo novamente
mydata2 = mydata2.set_index('Year')
print(mydata2)

