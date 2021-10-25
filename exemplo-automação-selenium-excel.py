from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
#1 Pegar a cotação do dolár
# entrar no site do google
navegador = webdriver.Chrome("chromedriver.exe")
navegador.get ("https://www.google.com")

# pesquisar a cotação do dólar
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do dolar')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegar a cotação da página do google
cotacao_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print (cotacao_dolar)

#2 Pegar a cotação do euro
navegador.get ("https://www.google.com")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print (cotacao_euro)
#3 Pegar a cotação do ouro ]
navegador.get ('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".")
print (cotacao_ouro)
#4 Importar a base de dados
tabela = pd.read_excel('Produtos.xlsx')
print(tabela)
#5 Mudar a cotação,preço de compra e o preço de venda
#cotaçao
tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)
#preço de compra = Preço * Cotação
tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Cotação"]
#preço de venda = Preço de compra * Margem
tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Margem"]
#6 Exportar o relatório atualizado
tabela.to_excel("tabela.xlsx",index=False)
navegador.quit()
# Instalar o Selenium
# Baixar o webdriver
# Instalar o chrome driver  na mesma pasta do código

