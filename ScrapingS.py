import time
from selenium import webdriver
import re
import json
# acceder a la path de chrom dirver
driver = webdriver.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')




# acceder a ala  mon sit GIT
driver.get('http://www.airindia.in/contact-details.htm')


doc = driver.page_source
emails = re.findall(r'[\w\.-]+@[\w\.-]+' , doc)
listeE = []
for email in emails:
    e = {}
    e["Email"] = email
    listeE.append(e)
    with open ('ScrapingE.json' , 'w') as ecrite:
        ecrite.write(json.dumps(listeE,indent = 4, sort_keys = True))
    print(email)



#  aficher le chrom et l nome de cette site sur la finctione .title
# print(driver.title)
#  .quit cette finction pour closer cette page aprais la exucutions
# driver.quit()

