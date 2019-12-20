import numpy as np 
import pandas as pd 
import pandas_datareader as pdr 

#Leia o arquivo Salaries.csv como um DataFrame chamado "sal"
sal = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\2. Python para análise de dados\Pandas\Pandas Exercises\Salaries.csv', index_col='Id')

#Verifique o "head" do DataFrame
print(sal.head())

#Use o método .info () para descobrir quantas entradas existem. 
print(sal.info())

#** Qual é o "BasePay" médio? **
print(sal['BasePay'].mean())

# Qual é a maior quantidade de "OvertimePay" no conjunto de dados?
print(sal['OvertimePay'].max())

#Qual é o cargo de JOSEPH DRISCOLL? Nota: use todas as maiúsculas, caso contrário você pode obter uma resposta que não coincida (há também um Joseph Driscoll com minúsculas)
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])

#Quanto JOSEPH DRISCOLL ganha (incluindo benefícios)?
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

#Qual o nome da pessoa mais bem paga (incluindo benefícios)?
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName'])

#Qual o nome da pessoa paga mais baixa (incluindo benefícios)? Você percebe algo estranho sobre o quanto ele ou ela é paga?
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()][['EmployeeName','TotalPayBenefits']])
#tem que se passar uma lista para fazer multiplas colunas [[A,B]] e não [A,B]

#Qual foi a média (média) BasePay de todos os funcionários por ano? (2011-2014)?
print(sal.groupby('Year').mean()['BasePay'])

#Quais títulos de trabalho únicos existem?
print(sal['JobTitle'].unique())
#QUANTOS títulos de trabalho únicos existem?
print(sal['JobTitle'].nunique())
#ou
print(len(sal['JobTitle'].unique()))

# Quais são os 5 principais empregos mais comuns?
print(sal['JobTitle'].value_counts().head(5))
#ou 
print(sal['JobTitle'].value_counts().iloc[:5])
#o método value counts já ordena em ordem de maior para o menor

#Quantos Títulos de Trabalho foram representados por apenas uma pessoa em 2013? (Por exemplo, títulos de trabalho com apenas uma ocorrência em 2013?) 
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))

#Quantas pessoas têm a palavra Chefe em seu cargo? (Isso é bastante complicado)
#formando a funçao
def chefe_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
#aplicando a condicional para fazer a soma
print(sum(sal['JobTitle'].apply(lambda x: chefe_string(x))))

#Bônus: Existe uma correlação entre o comprimento da seqüência do título do trabalho e o salário? 
#criando a coluna com os comprimentos do nome do cargo
sal['JobLength'] = sal['JobTitle'].apply(len)
print(sal['JobLength'])
#descobrindo se há correlação
print(sal[['JobLength','TotalPayBenefits']].corr())