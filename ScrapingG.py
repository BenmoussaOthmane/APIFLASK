from selenium import  webdriver as wb

##### SCRPAING WITH ID 

driver = wb.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://www.google.com/')

try:
    g = driver.find_element_by_id('gbw').text
    print("kayan ; " +g)
except Exception as e:
    print ("makanch ")


driver.close()




# /Users/benmoussaothmane/Downloads/chromedriver