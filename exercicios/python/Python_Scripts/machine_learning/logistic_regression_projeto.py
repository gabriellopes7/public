#Projeto de regressão logistica
#verificar se um usuario de internet clicou ou não em uma propaganda
#vamos criar um modelo que preveja se irá ou não clicar em um anúncio no futuro
# Daily Time Spent on Site': tempo no site em minutos.
# 'Age': idade do consumidor.
# 'Area Income': Média da renda do consumidor na região.
# 'Daily Internet Usage': Média em minutos por di que o consumidor está na internet.
# 'Linha do tópico do anúncio': Título do anúncio.
# 'City': Cidade do consumidor.
# 'Male': Se o consumidor era ou não masculino.
# 'Country': País do consumidor.
# 'Timestamp': hora em que o consumidor clicou no anúncio ou janela fechada.
# 'Clicked on Ad'': 0 ou 1 indicam se clicou ou não no anúncio.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

ad = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\5. Machine Learning\Regressão Logística\advertising.csv')
print(ad.head())
print(ad.info())
print(ad.columns)

# Crie um histograma de "Age
sns.set_style('whitegrid')
ad['Age'].hist(bins=30)
plt.xlabel('Age')
plt.show()



#Crie um joinplot mostrando "Area Income" versus "Age"
sns.jointplot('Age','Area Income',data=ad)
plt.show()


#Crie um jointplot que mostre as distribuições KDE do "Daily Time spent" no site vs "Age".
sns.jointplot('Age','Daily Time Spent on Site',data=ad,color='red',kind='kde')
plt.show()


#Crie um jointplot do 'Daily Time Spent on Site' vs. 'Daily Internet Usage
sns.jointplot('Daily Internet Usage','Daily Time Spent on Site',data=ad,color='green')
plt.show()

#Finalmente, crie um parplot com o matiz definido pelo recurso de coluna 'Clicked on Ad'
#sns.pairplot(ad,hue='Clicked on Ad',diag_kind='hist') #muito pesado
#plt.show()

# Divida os dados em conjunto de treinamento e conjunto de testes usando train_test_split
sns.heatmap(ad.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show() #dados 100% preenchidos

from sklearn.metrics import classification_report as cr 
from sklearn.metrics import confusion_matrix as cm
from sklearn.linear_model import LogisticRegression as lr 
from sklearn.model_selection import train_test_split as tts 


country = pd.get_dummies(ad['Country'],drop_first=True)
ad.drop('Country',inplace=True,axis=1)
ad = pd.concat([ad,country],axis=1)
print(ad.head())

x_train,x_test,y_train,y_test=tts(ad.drop(['Clicked on Ad','City','Ad Topic Line','Timestamp'],axis=1),ad['Clicked on Ad'],test_size=0.3)
print(x_train.head())

logmodel = lr()
logmodel.fit(x_train,y_train)
predictions = logmodel.predict(x_test)
#classificando os acertos
print(cr(y_test,predictions))
print(cm(y_test,predictions))
