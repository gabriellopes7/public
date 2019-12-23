#Seaborn é uma biblioteca de visualização estatistica de dados
#possui excelentes padrões
#foi projetado para trabalhar em harmonia com objetos do tipo DataFrame do pandas
#padrões simples e bonitos de serem plotados


#galeria https://seaborn.pydata.org/examples/index.html

#pagina API para instruções das funções
import seaborn as sns
import matplotlib.pyplot as plt

#PLOTS Numéricos
#distplot
#jointplot
#pairplot
#rugplot
#kdeplot
#o Seaborn ja possui alguns datasets já carregados no seu conjunto

tips = sns.load_dataset('tips') #no site há outros datasets
print(tips.info()) #dados de gorgetas
print(tips.head())


#distplot -> cria um histograma e cria uma curva KDE
sns.distplot(tips['total_bill'])
plt.show()
#é possivel retirar a curva de Kernel
sns.distplot(tips['total_bill'], kde=False)
plt.show()
#alterando os valores das colunas do histograma
sns.distplot(tips['total_bill'],bins=50)
plt.show()
#Kernel Density Estimation (KDE)


#jointplot -> cria uma curva de distribuição parecida ao distplot, mas com duas variáveis
#ex: quero saber qual tipo de cliente que fornece mais gorgeta, dia da semana e 
#a relação que ele tem com o total da conta
sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()
#mudando o estilo
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
plt.show()
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex') #mostra cores mais fortes onde há maior conjunto de dados
plt.show()
#faz gráficos de distribuição conjunta


#pairplot -> pega todas as variáveis do dataset e faz joint plot de todas elas
sns.pairplot(tips)
plt.show()
#parametro hue
sns.pairplot(tips,hue='sex') #da cores diferentes para dados categóricos diferentes
plt.show()

#paleta de cores
sns.pairplot(tips,palette='coolwarm')
plt.show()


#rugplot -> ele é a base do KDE, se assemelha a uma distribuição
#coloca um traço pequeno onde há dados
#util para criar um KDE, serve para mostrar a distribuição de dados
#quando você não sabe o tipo de distribuição que ele segue
#KDE -> é uma forma não paramétrica para estimar funções de distribuição de probabilidade de
#uma variável aleatória.
sns.rugplot(tips['total_bill'])
plt.show()


#kdeplots
sns.kdeplot(tips['total_bill'])
plt.show()



#PLOTS Categóricos
#factorplot
#boxplot
#violinplot
#stripplot
#swarmplot
#barplot
#countplot

import numpy as np 


#barplot -> pede apenas dois inputs (x,y) e data
sns.barplot(x='sex',y='total_bill',data=tips)
plt.show()
#mostra o desvio padrão do conjunto de dados

#pode-se ver outros valores, com parâmetro estimator
sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)
plt.show()


#countplot -> conta os elementos daquele eixo - categoria
sns.countplot(x='sex',data=tips)
plt.show()

#boxplot-> plota percentil de dados para a gente
#de baixo para cima
#da barra inferior até a caixa: mostra onde estão concentrados 25% dos dados
#metade inferior da caixa: 50% dos dados
#metade superior: 75% dos dados
#barra superior: 100% dos dados
#os pontos acima são outliers, pontos que não são considerados dentro do cálculo
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()
#pode-se usar palette para mudar as cores também
#hue->quebra as categorias em outras
sns.boxplot(x='day',y='total_bill',hue='sex',data=tips)
plt.show()
#pode estar na horizontal
sns.boxplot(data=tips,palette='rainbow',orient='h')
plt.show()
#pega somente os dados numéricos e faz o boxplot com eles


#violinplot-> cria distribuição de probabilidade para o conjunto de dados baseado no modelo não
#paramétrico KDE
sns.violinplot(x='day',y='tip',data=tips)
plt.show()
#mostra a distribuição dos dados
#também é possível quebrar utilizando o hue e usar o split para aproveitar o espaço
sns.violinplot(x='day',y='tip',data=tips,hue='sex',split=True)
plt.show()


#stripplot -> plota apenas pontos onde os dados aparecem, tipo um rugplot
sns.stripplot(x='day',y='total_bill',data=tips) #neste caso o jitter já está True
#colocando o Jitter True, os pontos ficam mais espalhados para entender a densidade
#é possível usar o hue e split
plt.show()


#swarmplot -> é um stripplot com os pontos mais organizados, um do lado do outro
#ele lida muito mal com uma quantidade muito grande de dados
#também se pode usar hue e split

sns.swarmplot(x='day',y='total_bill',data=tips)
plt.show()

#combinação boa de swamplot com violinplot
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
sns.violinplot(x='day',y='total_bill',data=tips)
plt.show()

#factorplot -> permite que crie qualquer tipo de plot anterior, usando o parâmetro KIND
sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar') #cria um gráfico de barra
plt.show()




