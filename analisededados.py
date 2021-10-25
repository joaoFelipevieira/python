


# - Entender quais as informações estão disponiveis
# - Descobrir as cagadas da base de dados






#pandas,numpy,openpyxl

#1 Importar a base de dados
import pandas as pd
import plotly.express as px
tabela = pd.read_csv ("telecom_users.csv")

#2 Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0" , axis=1)
print (tabela)

#3 Tratamento de dados


#- Valores que estão sendo reconhecidos de forma errada
tabela ["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors = "coerce")

# deletando as colunas vazias
tabela = tabela.dropna(how="all",axis = 1)
# deletando linhas vazias
tabela = tabela.dropna(how="any",axis = 0)


print (tabela.info())
#4 Análise inicial
# Como estão nossos cancelamentos?
print (tabela["Churn"].value_counts())
print (tabela["Churn"].value_counts(normalize=True))
#5 Análise completa
#comparar cada coluna da minha tabela com a coluna de cancelamento
#criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    #exibir o gráfico
    grafico.show()
