#Regressão linear permite que a gente crie modelos que utilizem 
#relações lineares entre algumas variáveis para predizer o valor de uma terceira variável
#O objetivo da regressão linear é minimizar a distância vertical entre os pontos até a linha
#Biblioteca SciKit-Learn e Python para criar um modelo de regressão linear

#Prever o preço das casas baseado em suas características
# Podemos trabalhar com dados da Kaggle que são dados reais
#pip install scikit-learn
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

USAHousing = pd.read_csv(r'D:\Documentos\public\exercicios\python\Python_Scripts\machine_learning\rock_forecasts\USA_Housing.csv')
print(USAHousing.info())
print(USAHousing.columns)

#fazendo um pairplot para visualizar a disponibilização dos dados
sns.pairplot(USAHousing)
#plt.show() #as vezes é mais interessante usar o Anaconda
#é possível perceber a relação linear entre os dados e o preço
sns.heatmap(USAHousing.corr(),cmap='rainbow')
#heatmap para perceber a relação linear
plt.show()

#parâmetros X 
#Y o que será predito
x = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']] #todos menos preço
y = USAHousing['Price'] #-> preço será predito

#importando um método do scikit-learn, capaz de fazer o split dos dados X e Y em treino e teste
from sklearn.model_selection import train_test_split as tts 
x_train, x_test, y_train, y_test = tts(x,y,test_size=0.4,random_state=101) #quebra os dados em proporções iguais
#inputs->x(parametros), y(saídas),test_size(quantos % serão em tamanho de teste)
#random_state = ele escolhe um algoritmo aleatorio para fazer a divisão, escolhendo um numero, vc tem uma
#divisão específica
#tts vai retornar uma tupla no formato (A,B,C,D)
#A = X treino, B = X teste, C = Y treino, D = Y teste
#mostrando que foi dividido em 60/40% - são 5 mil dados
print(x_train.shape[0]) #3000
print(x_test.shape[0]) #2000

#criar uma instancia da classe que contem o modelo que queremos utilizar
#para modelo linear
from sklearn.linear_model import LinearRegression as lr 
lm = lr() #criando a instância
lm.fit(x_train,y_train) #fit -> encontrar os parametros para o modelo linear, passando parâmetro um x de treino,
#e um y de treino como resposta

print(lm.intercept_) #onde cruza o eixo Y
print(lm.coef_) #coeficiente de cada variável
coefs = pd.DataFrame(lm.coef_,x.columns,columns=['Coefs'])
print(coefs) #cada 1 acrescimo de unidade de cada variável, causa um acrescimo de preço na unidade que aparece
#não faz muito sentido, mas é o que ele aprendeu com o x e y de treinamento

#método para prever os valores de y, baseado no x de teste
predict = lm.predict(x_test)
print(predict)

#agora é necessário verificar a eficiência das previsões
plt.scatter(y_test,predict) #se o gráfico traçar uma linha reta, a previsão foi perfeita
plt.show() #mostrará um gráfico linear comparando o real com o previsto, 
#se estiver próximo de uma linha reta, quer dizer que o modelo foi razoavelmente eficaz
#outra forma de verificar a acurácia
#gráfico de distribuição dos erros, resíduos
sns.distplot(y_test-predict) #mostra que os erros ficam bem próximos de zero
# uma cauda não pode estar maior que a outra    
plt.show() #se mostra uma distribuição normal, mostra a eficácia no modelo

#outras métricas de calcular as distorções
#3 métricas padrões
#MAE, MSE, RMSE
#MAE (Mean Absolute Error) -> erro absoluto médio, é basicamente o que mostra no distplot
#calcula a diferença entre a média das diferenças entre todos os valores preditos e os valores corretos

#MSE (Mean Squared Error) -> média do quadrado do erro, todos os erros, as diferenças entre
#as prediçoes e valor real te eleva ao quadrado e soma, muito boa para indicar modelos superiores a outros

#RMSE (Root Mean Squared Error) -> raiz quadrada da média dos erros quadrados
#é a raiz quadrada do MSE

#importando a classe que calcula as métricas de distorçoes
from sklearn import metrics
#MAE
print('MAE',metrics.mean_absolute_error(y_test,predict)) #coloca 2 parâmetros, o real seguido da previsão
#erro médio de 82 mil dólares
#MSE
print('MSE: ',metrics.mean_squared_error(y_test,predict))
#RMSE
print('RMSE: ',np.sqrt(metrics.mean_squared_error(y_test,predict)))
#erro de 102 mil dólares médio