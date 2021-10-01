#libraries
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium
# pip install webdriver-manager

# Code By: Ítalo Magalhães
# E-mail: italo.ufsj@gmail.com


import time
import pandas as pd
from bs4 import BeautifulSoup, element
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Pegar o conteudo HTML apartir da pagina
url = "http://idebescola.inep.gov.br/ideb/consulta-publica"

#Abrir o Firefox com o link acima
driver =  webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get(url)
time.sleep(5)

inputElement = driver.find_element_by_id("pkCodEntidade")

#inserindo o codigo da escola
inputElement.send_keys("codigo_escola")

time.sleep(3)
#realizando a ação de apertar o botão
inputElement.submit() 

time.sleep(3)

#localizando a tabela de informações
elemento = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[3]/div/table")
#extraindo seu conteudo
html_content = elemento.get_attribute('outerHTML')

#2) Parsear conteudo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#3) Estruturas conteudo em um data frame - Pandas
df_full = pd.read_html(str(table))[0]

# 4) Salvando em um csv
print(df_full)
df_full.to_csv('dataBase.csv', index=False, encoding='latin1')

driver.quit()


