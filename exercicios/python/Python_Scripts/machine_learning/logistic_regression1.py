#Regressão Logística
#método de classificação
#Exemplos de problemas a serem resolvidos
#Filtros de emails
#Modelos preditores de clientes inadimplentes
#Diagnóstico de doenças

#Apesar de confuso, a regressão logística nos permite resolver
#problemas de classificação onde estamos tentando predizer categorias discretas

#Por convençao, classificações binárias terão duas classes, 0 e 1
#Regressao logistica lida melhor com a teoria da probabilidade
#sempre com valores entre 0 e 1
#baseada na função sigmóide, que só retorna valores entre 0 e 1
#Também utilizado dentro de redes neurais
#Os valores são interpretados como a probabilidade da classe ser 0 ou 1
#Se estiver acima de 0,5 é 1
#Se estiver abaio de 0,5 é 0
#Após treinarmos um modelo de regressão logística, testamos o mesmo em um conjunto de dados
#de teste. Porém as métricas de avaliação de desempenho são diferentes da regressão linear

#A principal forma de avaliá-lo é suar uma MATRIZ DE CONFUSÃO
#MATRIZ DE CONFUSÃO
#Valor correto (SIM/NÃO) 
#Valor predito (SIM/NÃO)
#Terminologia: O output são 4
#TRUE -> quando o preditivo acerta
#True Positive(TP) -> Positivo verdadeiro, preditivo verdadeiro e teste verdadeiro
#True Negative (TN) -> Negativo verdadeiro, preditivo fala que é falso e teste está falso
#FALSE -> quando o modelo erra
#False Positive (FP) -> Falso positivo, preditivo fala que é verdadeiro mas o teste é falso
#False Negative (FN) -> Falso negativo, preditivo fala que é falso, mas o teste é verdadeiro (PIOR CASO) 
# Precisão:
# Cálculo: Total de TRUES dividido pelo total de testes
# TP+TN/Total
# Erros:
# FP+FN/Total
# Erro do tipo 1: Predição fala que é verdadeiro, mas é falso
# Erro do tipo 2: Quando o fala que é falso, mas é verdadeiro
