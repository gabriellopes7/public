#https://www.kaggle.com/ 
#portal de datasets para estudar analise de dados e machine learning
#há competicoes no site de machine learning

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r'Python-Data-Science-and-Machine-Learning-Bootcamp\4. Projetos de dados\911.csv')
print(df.head())
print(df.info())

#os 5 códigos postais mais ligados
print(df['zip'].value_counts().head(5))


print(df['twp'].value_counts().head(5))

#quantos tipos diferentes de title existem
print(df['title'].nunique())

#criando a coluna reasons somente com o título da categoria
df['reasons'] = df['title'].apply(lambda x: x.split(':')[0])
print(df['reasons'])

#** Qual é o motivo mais comum para uma chamada do 911 com base nessa nova coluna? **
print(df['reasons'].value_counts())


#** Agora use Seaborn para criar um countplot de chamadas 911 baseadas nesta nova coluna. **
import seaborn as sns 
sns.countplot(x='reasons',data=df)
plt.show()

#Agora vamos começar a focar em informações de tempo. 
# Qual é o tipo de dados dos objetos na coluna timeStamp? **
print(type(df['timeStamp'].iloc[0]))
print(df['timeStamp'])
#convertendo timestamp de string para datetime
df['timeStamp']= pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'].iloc[0]))

#Agora que a coluna timestamp é realmente objetos DateTime, use .apply () 
# para criar 3 novas colunas chamadas Hour, Month e Day of Week. 
# Você criará essas colunas com base na coluna timeStamp, consulte as soluções se 
# você ficar preso nesta etapa. **
df['Hour']=df['timeStamp'].apply(lambda x: x.hour)
print(df['Hour'].iloc[0])

df['Month']=df['timeStamp'].apply(lambda x: x.month)
print(df['Month'].iloc[0])

df['Day of week']=df['timeStamp'].apply(lambda x: x.dayofweek)
print(df['Day of week'].iloc[0])

#Observe como o dia da demana é um número inteiro de 0-6. Use o 
# .map () com este dicionário para mapear os nomes das seqüências reais para o dia da semana: 
#dicionario de dias de semana
dmap={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of week']=df['Day of week'].map(dmap)
print(df['Day of week'].iloc[0])

#** Agora use Seaborn para criar um countplot da coluna "Day of Week" 
# com a tonalidade baseada na coluna Reason. **
sns.countplot(x='Day of week',hue='reasons',data=df)
plt.show()

#mesmo para o mês
sns.countplot(x='Month',hue='reasons',data=df)
#não apareceram alguns meses
plt.show()

#Agora, crie um objeto groupby chamado "byMonth", 
# onde você agrupa o DataFrame pela coluna do mês e use o método count() para agregação. 
# Use o método head() neste DataFrame retornado. **
byMonth = df.groupby('Month').count()
print(byMonth.head())

#Agora crie um plot simples fora do Dataframe indicando a contagem de chamadas por mês
byMonth['twp'].plot()
plt.show()
#Agora veja se você pode usar o lmplot () do Seaborn para criar um modelo linear no número de chamadas por mês. 
# Tenha em mente que talvez seja necessário resetar o índice em uma coluna
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()

#Crie uma nova coluna chamada 'Data' que contenha a data da coluna timeStamp.
#  Você precisará usar .apply() junto com o método .date()
df['Data'] = df['timeStamp'].apply(lambda x: x.date())
print(df['Data'].iloc[0])

#Agora agrupe esta coluna Data com o groupby.
#  Usando o count (), crie um gráfico de contagens de chamadas 911
df.groupby('Data').count()['twp'].plot()
plt.tight_layout()
plt.show()

# Agora recrie esse plot, mas crie 3 
# plots separados com cada plot representando uma Razão para a chamada 911
df[df['reasons']=='Traffic'].groupby('Data').count()['twp'].plot()
plt.title('Traffic')
plt.show()
df[df['reasons']=='EMS'].groupby('Data').count()['twp'].plot()
plt.title('EMS')
plt.show()
df[df['reasons']=='Fire'].groupby('Data').count()['twp'].plot()
plt.title('Fire')
plt.show()

#Agora vamos continuar a criar mapas de calor com seaborn e nossos dados. 
# Em primeiro lugar, devemos reestruturar o quadro de dados para que as colunas se tornem horas e o Índice se torne o Dia da Semana. 
# Há muitas maneiras de fazer isso, mas eu recomendaria tentar combinar groupby com o método unstack . 
# Consulte as soluções se você ficar preso nisso! **

#criando uma nova base de dados agrupando por dia da semana e hora, com a contagem de motivos
dayHour = df.groupby(by=['Hour','Day of week']).count()['reasons'].unstack()
print(dayHour.head())

#Agora crie um mapa de calor usando este DataFrame 
sns.heatmap(dayHour,cmap='YlGnBu')
plt.show()
sns.heatmap(dayHour,cmap='viridis')#outro estilo
plt.show()

sns.clustermap(dayHour,cmap='viridis')
plt.show()

# Agora repita estes mesmos plots e operações para um DataFrame que mostra o mês como a coluna.
dayMonth=df.groupby(by=['Month','Day of week']).count()['reasons'].unstack()
print(dayMonth.head())
sns.heatmap(dayMonth,cmap='BuPu')
plt.show()
sns.clustermap(dayMonth,cmap='Greens')
plt.show()