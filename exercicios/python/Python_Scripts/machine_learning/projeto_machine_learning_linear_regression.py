# #Parabéns! Você obteve algum contrato de trabalho com uma empresa de comércio eletrônico com sede na cidade de Nova York que vende roupas online, mas também tem sessões de consultoria em estilo e vestuário na loja.
#  Os clientes entram na loja, têm sessões / reuniões com um estilista pessoal, então podem ir para casa e encomendarem em um aplicativo móvel ou site para a roupa que desejam.
# A empresa está tentando decidir se deve concentrar seus esforços em sua experiência em aplicativos móveis ou em seu site. 
# Eles contrataram você no contrato para ajudá-los a descobrir isso! Vamos começar!
# Basta seguir as etapas abaixo para analisar os dados do cliente 
# (é falso, não se preocupe, eu não lhe dei números reais de cartões de crédito ou e-mails).
#Importe pandas, numpy, matplotlib,e seaborn. 
# Em seguida, configure% matplotlib inline (Você importará sklearn conforme você precisar). **
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

ecData = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\5. Machine Learning\Regressões Lineares\Ecommerce Customers')
print(ecData.head())
print(ecData.info())
print(ecData.columns)

# Use seaborn para criar um jointplot para comparar as colunas Time On Website e Volume anual.
#  A correlação faz sentido? **
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=ecData)
plt.show()

#Faça o mesmo, mas com a coluna tempo no aplicativo (Time on App), em vez disso
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=ecData)
plt.show()

# Use jointplot criar um lote de caixa hexagonal 2D que compara tempo no aplicativo (Time on App) 
# e o tempo da associação (Length of Membership).
sns.jointplot(x='Time on App',y='Length of Membership',data=ecData,kind='hex')
plt.show()

#Vamos explorar esses tipos de relações em todo o conjunto de dados. 
# Use parplot para recriar o gráfico abaixo. (Não se preocupe com as cores)
sns.pairplot(ecData)
plt.show()

#Crie um plot de um modelo linear (usando o lmplot de Seaborn) 
# da quantia anual gasta (Yearly Amount Spent) vs. tempo de associação (Length of Membership). **
sns.lmplot(x='Yearly Amount Spent',y='Length of Membership',data=ecData)
plt.show()

#Agora que exploramos um pouco os dados, vamos avançar e dividir os dados em conjuntos de treinamento e teste.
#  ** Defina uma variável X igual a todas as características 
# numéricas dos clientes e uma variável y igual à coluna Valor anual gasto (Yearly Amount Spent). **
x=ecData[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y=ecData['Yearly Amount Spent']
print(x.columns)

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
#Em cada aumento de unidade em cada parâmetro correponde a um aumento de X dólares por ano
#A empresa precisa se concentrar em fidelizar o seu cliente pelo dobro de influencia
#Dentre site e app, o aplicativo tem um impacto muito maior do que o site
