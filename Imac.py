import requests
from bs4 import BeautifulSoup
import json


aceder  = requests.get('https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=Imac&N=-1&isNodeId=1')

code =  aceder.content

proced = BeautifulSoup(code, "html.parser")

all  = proced.find_all("div" , {"class":"item-container"} )

liste = []
sum  = 0
for item in all : 
    dico = {}
    try:
        sum +=1
        dico["Id"] = sum
    except : 
        dico["Id"] = None
    
    try:
        dico["Name"] = item.find("a" , {"title" :"View Details"}).text.replace("\"" ,"")
    except:
        dico["Name"] = None
    try:
        dico["price"] = item.find("li" , {"class":"price-current"}).text.replace("\r" , "").replace("\n" ,"").replace("/u" , "").replace("\u00a0            \u2013" ,"").replace("\xa0(3 Offers)–" ,"").replace("\u00a0(2 Offers)\u2013" ,"").replace("\u00a0(1 Offers)\u2013" ,"").replace("\u00a0(5 Offers)\u2013" ,"").replace("|","")
    except:
        dico["price"] = None
    try:
        dico["Etiol"] = item.find("span" , {"class":"item-rating-num"}).text.replace("(" , "").replace(")" ,"")
    except:
        dico["Etiol"] = None
    liste.append(dico)
    print(dico)

    with open("Imac.json" , "w") as icrote:
        icrote.write(json.dumps(liste ,indent = 4, sort_keys = True))
