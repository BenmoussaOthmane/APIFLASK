import time
from selenium import webdriver


driver = webdriver.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://github.com/BenmoussaOthmane')

print(driver.title)
driver.quit()

