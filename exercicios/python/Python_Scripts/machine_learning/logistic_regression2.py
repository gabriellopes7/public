#Projet regressão logística
#Usando dados do titanic da kaggle para predição de passageiros que sobreviveram e morreram no desastre
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

train = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\5. Machine Learning\Regressão Logística\titanic_train.csv')
print(train.head())
print(train.columns)

test =  pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\5. Machine Learning\Regressão Logística\titanic_test.csv')
print(test.head())
print(test.columns)

print(train.isnull()) #verifica quais dados são null no dataset
#fazendo um heatmap ajuda a verificar
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
#mostra que cabine e idade tem valores nulos
#os de cabine está faltando muitos, deve ser descartado
#embarcado apenas 1
#idade faltando alguns 30%, precisamos tratar

#Análise exploratória de dados
sns.set_style('whitegrid')
#fazendo countplot de passageiros que sobreviveram ou não
sns.countplot(x='Survived',data=train)
plt.show()
#segregando por sexos
sns.countplot(x='Survived',data=train, hue='Sex',palette='RdBu_r')
plt.show()
#mostra a maioria de sobreviventes foram mulheres
#agora segregando pela classe no navio
sns.countplot(x='Survived',data=train,hue='Pclass',palette='rainbow')
plt.show()

#distribuição de idades
#maioria entre 20 e 30 anos e boa quantidade de crianças
train['Age'].hist(bins=30,color='darkred',alpha=0.4)
plt.show()

#distribuição de pessoas que acompanhavam os passageiros no navio
sns.countplot(x='SibSp',data=train)
plt.show()
#maioria desacompanhado

#verificar a relação entre idade e pessoas acompanhadas
train[train['SibSp']==0]['Age'].hist(bins=30)
plt.show()
#vendo os passageiros desacompanhados, a maioria está entre 22 e 23 anos

#visualizar a distribuição de preço dos tickets
train['Fare'].hist(color='green',bins=50,figsize=(12,6))
plt.show()
#maioria pagou baixos preços, abaixo de 100

#visualizar os preços baixos
train[train['Fare']<70]['Fare'].hist(color='red',bins=50,figsize=(12,6))
plt.show()
#maioria pagou 7 dólares, sem correção da inflação

#para encaixar os dados no machine learning, precisamos tratar os dados faltantes e problematicos
#tratando os dados faltantes
plt.figure(figsize=(12,6))
sns.boxplot(x='Pclass',y='Age',data=train)
plt.show()

#mostra que pessoas de classe mais baaixa são mais velhas, e classe alta, mais novas
#há tres tipos de abordagens possíveis
#podemos deletar todos os valores(mas não é interessante)
#preencher os valores para não atrapalhar as predições
#preencher as idades de acordo com uma média
#fazendo função para tratar os dados
#Inserindo os dados faltantes na idade, como a média de idade da classe daquela pessoa
def inputar_idade(cols):
    idade=cols[0]
    classe=cols[1]

    if pd.isnull(idade):
        if classe==1:
            return 37 #média da idade de pessoas da classe 1
        elif classe==2:
            return 29 #média de idade da classe 2
        else:
            return 24 #media de idade da classe 3
    else:
        return idade
train['Age'] = train[['Age','Pclass']].apply(inputar_idade,axis=1)
#refazendo o heatmap para ver como ficou a idade
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
#não há mais dados faltantes em idade

#tratando cabine, mas tem tanta informação faltante que é melhor descartá-la
del train['Cabin']
#ou train.drop('Cabin', inplace=True) -> ambas fazem a mesma coisa

#refazendo o heatmap para verificar
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

#falta somente o individuo sem valor
train.dropna(inplace=True) #->apaga linhas que contem qualquer tipo de informação falsa
#por padrão ele apaga linha axis=0, se eu quisesse apagar coluna, deveria inserir axis=1
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
#verificando o novo heatmap

#tratando os dados para tratar no machine learning
#agora é necessário alterar os dados categóricos, transformando-os em números e não strings
#nome não será utilizado
#ticket tbm não
#pd.get_dummies() -> transforma uma coluna com strings e transforma em dado binário

print(pd.get_dummies(train['Sex'])) #-> transforma male em coluna e female em coluna de 0 e 1
#porem gera duas colunas desnecessárias, pois se male for 0, a pessoa é female
#para isso, retiramos uma das colunas com o drop_first=True
sex = pd.get_dummies(train['Sex'],drop_first=True )

print(train['Embarked'].value_counts()) #para ver a quantidade de possibilidades de embarked
#tem tres possibilidaeds, fazemos um get_dummies
embark = pd.get_dummies(train['Embarked'],drop_first=True) #tambem fazendo um drop first, pois 0 e 0 dos dois significa 1 no terceiro

#excluindo variáveis não necessárias no dataset
#passenger id, name, sex(iremos adicionar o novo), ticket e embarked(iremos substituir)
train.drop(['Sex','PassengerId','Name','Embarked','Ticket'],axis=1,inplace=True) 
#inplace serve para substituirmos definitivamente o valor no dataset
print(train.head())
train = pd.concat([train,sex,embark],axis=1) #especificar que axis = 1 para inserir novas colunas
print(train.head(50))
#o modelo deve estar todo numérico

#calibrando o modelo
from sklearn.linear_model import LogisticRegression
#quebrar os dados em dados de treino e de teste
from sklearn.model_selection import train_test_split as tts 
x_train, x_test, y_train, y_test = tts(train.drop('Survived',axis=1),train['Survived'],test_size=0.3) #não utilizar o inplace para não deixar definitivo

#criando instancia da regressao logistica
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
predictions=logmodel.predict(x_test)
#pegando as métricas para regressão logistica
from sklearn.metrics import classification_report as cr 
print(cr(y_test,predictions)) #acertou mais de 50% e acertou mais quem morreu do que quem sobreviveu

#importanto a matriz de confusão
from sklearn.metrics import confusion_matrix as cm 
print(cm(y_test,predictions)) #olhamos o valor da diagonal, que são Predito/Correto = Não, Predito/Correto = Sim


