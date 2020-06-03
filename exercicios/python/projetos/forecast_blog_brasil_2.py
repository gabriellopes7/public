import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

def int_comma(val):
  """
  Convert the sessions string to int value
  Ex.: 1,757 -> 1757
  - Remove , from the number
  - Convert to int
  """
  new_val = val.replace(',','')
  return int(new_val)

blogData = pd.read_csv(r'D:\Documentos\public\exercicios\python\Python_Scripts\machine_learning\rock_forecasts\blog_brasil.csv',skiprows=6,parse_dates=['Day'])
blogData['Sessions'] = blogData['Sessions'].apply(int_comma)
blogData.info()
blogData['Day'] = pd.to_numeric(blogData['Day'])
blogData.info()
X = blogData.iloc[:,0].values
Y = blogData.iloc[:,1].values
X
Y
correlacao = np.corrcoef((X,Y))
correlacao