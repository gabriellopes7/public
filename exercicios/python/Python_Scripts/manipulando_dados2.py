import pandas as pd 
import numpy as np 

ecom = pd.read_csv(r'C:\Users\Gabriel Ladeira\Documents\python_data_science\Python-Data-Science-and-Machine-Learning-Bootcamp\2. Python para análise de dados\Pandas\Pandas Exercises\Ecommerce Purchases')

#Verifique o "head" do DataFrame.
print(ecom.head())

#** Quantas linhas e colunas existem? **
print(ecom.info())
#retorna somente linhas e colunas \/
print(ecom.shape)
#retorna a quantidade de linhas
print(len(ecom))

#mostrar as colunas
print(ecom.columns)

#Qual é o preço de compra médio?
print(ecom['Purchase Price'].mean())

#Quais foram os preços de compra mais altos e mais baixos? **
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

#Quantas pessoas têm Inglês 'en' como sua língua de escolha no site? **
print(sum(ecom['Language'] == 'en'))
print(ecom[ecom['Language'] == 'en']['Language'].count())

# Quantas pessoas têm o cargo de "Advogado"? **
print(sum(ecom['Job'] == 'Lawyer'))


#** Quantas pessoas fizeram a compra durante a AM e quantas pessoas fizeram a compra durante o PM? **
#** (Sugestão: Confira value_counts ()) **
print(ecom['AM or PM'].value_counts())

# Quais são os 5 títulos de trabalho mais comuns? 
print(ecom['Job'].value_counts().head(5))

#Alguém fez uma compra que veio do Lot: "90 WT", qual foi o preço de compra para esta transação?
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# Qual é o email da pessoa com o seguinte número do cartão de crédito: 4926535242672853 
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# Quantas pessoas têm o American Express como seu fornecedor de cartão de crédito 
# #* e * fizeram uma compra acima de US $ 95? **
print(sum(ecom[ecom['Purchase Price']>95]['CC Provider']=='American Express'))

#Difícil: quantas pessoas tem um cartão de crédito que expira em 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')))

#Difícil: quais são os 5 principais 
#provedores de e-mail / hosts mais populares (por exemplo, gmail.com, yahoo.com, etc ...)
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))