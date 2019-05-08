from selenium import webdriver 
import re


driver = webdriver.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://airalgerie.dz/contacts/')

doc  = driver.page_source

tel = re.findall(r'[+][]?[\d]{3} [\d]{2} [\d]{2} [\d]{2} [\d]{2}',doc)


for nbr in tel :
    print(nbr)
