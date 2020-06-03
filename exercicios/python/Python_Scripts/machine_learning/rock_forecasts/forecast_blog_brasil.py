#Analise de forecast dos dados do blog brasil Rock Content desde 2016 usando regressão linear
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

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
type(blogData['Day'][0])

print(blogData.head())
print(blogData.info())
print(blogData.columns)


start_date = '01-01-2016'
end_date = '12-31-2019'
mask = (blogData['Day'] > start_date) & (blogData['Day'] <= end_date)
blog2019 = blogData.loc[mask].copy()
blog2019

type(blog2019['Day'])
    
# =============================================================================
# print(type(pd.Series.to_string(blog2019['Day'])))
# import time
# from datetime import datetime
# time.mktime(datetime.strptime(pd.Series.to_string(blog2019['Day']), '%Y-%m-%d').timetuple())
# =============================================================================

print(blog2019.head())
print(blog2019.info())
print(blog2019.columns)



# Use seaborn para criar um jointplot para comparar as colunas Day e Sessions.
#  A correlação faz sentido? **
sns.jointplot(x='Day', y='Sessions',data=blogData)
plt.show()

sns.jointplot(x='Month',y='Sessions',data=blogData)
plt.show()

sns.jointplot(x='Year',y='Sessions',data=blogData)
plt.show()

sns.jointplot(x='Day',y='Sessions',data=blogData)
plt.show()



# Use jointplot criar um lote de caixa hexagonal 2D que compara dia por sessões
sns.jointplot(x='Day',y='Sessions',data=blogData,kind='hex')
plt.show()

#Vamos explorar esses tipos de relações em todo o conjunto de dados. 
# Use parplot para recriar o gráfico abaixo. (Não se preocupe com as cores)
sns.pairplot(blog2019)
plt.show()

#Crie um plot de um modelo linear (usando o lmplot de Seaborn) 
# de data por Sessoes. **
sns.lmplot(x='Day',y='Sessions',data=blog2019)
plt.show()


#trocando os outliers por media
media = blog2019.loc[blog2019['Sessions']<73000,'Sessions'].mean()
blog2019['Sessions']=np.where(blog2019['Sessions']>73000,media,blog2019['Sessions'])
sns.lmplot(x='Day',y='Sessions',data=blog2019)
plt.show()



#Agora que exploramos um pouco os dados, vamos avançar e dividir os dados em conjuntos de treinamento e teste.
#  ** Defina uma variável X igual a todas a data
# e y igual a sessions **
x=blog2019['Day']
y=blog2019['Sessions']
print(x)

#Use model_selection.train_test_split da sklearn para dividir os 
# dados em conjuntos de treinamento e teste. Defina test_size = 0.3 e random_state = 101 **
from sklearn.model_selection import train_test_split as tts 
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.3,random_state=101)

#Agora é hora de treinar nosso modelo em nossos dados de treinamento!
#** Importe LinearRegression do sklearn.linear_model **
from sklearn.linear_model import LinearRegression as lrs 

#criando instancia do linear regression
lm = lrs()
#Treine LM nos dados de treinamento com lm.fit()
lm.fit(x_train,y_train)
print(lm.intercept_)
print(lm.coef_)

#Agora que nos ajustamos ao nosso modelo, 
# vamos avaliar o seu desempenho ao prever os valores de teste!
#** Use lm.predict () para prever o conjunto X_test dos dados. **
prediction = lm.predict(x_test)
print(prediction)

#Crie um diagrama de 
# dispersão (scatterplot) dos valores reais de teste em relação aos valores preditos.
sns.scatterplot(x=y_test,y=prediction)
plt.xlabel('Y test')
plt.ylabel('Prediction')
plt.show()
#foi quase uma linha perfeita


#* Calcule o erro absoluto médio, o erro quadrado 
# médio e o erro quadrado médio da raiz. Consulte a palestra ou a Wikipédia para as fórmulas **
from sklearn import metrics
print('MAE: ', metrics.mean_absolute_error(y_test,prediction))
print('MSE: ', metrics.mean_squared_error(y_test,prediction))
print('RMSE: ',np.sqrt(metrics.mean_squared_error(y_test,prediction)))

#Resíduos
#Trace um histograma dos resíduos e certifique-se de que ele parece normalmente distribuído. 
# Use o seaborn distplot, ou apenas o plt.hist ().#distplot
sns.distplot(y_test-prediction)
plt.show()


coefs=pd.DataFrame(lm.coef_,x.columns,columns=['Coefs'])
print(coefs)
#Em cada aumento de unidade em cada parâmetro correponde a um aumento de X sessions por ano

