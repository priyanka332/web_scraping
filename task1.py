import requests
from bs4 import BeautifulSoup
import json
user=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
data=BeautifulSoup(user.text,"html.parser")
def moviedata():
    list=[]
    mainDiv=data.find("div",class_="body_main container")
  
    subDiv=mainDiv.find("table",class_="table")
   
    tableall=subDiv.find_all('tr')
   
    for i in tableall:
        alltds=i.find_all('td')
        d={}
        for j in alltds:
            rank=i.find('td',class_="bold").get_text()[:-1]
            d["rank"]=int(rank)
           
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            d["rating"]=int(rating)
           
            review=i.find("td",class_="right hidden-xs").get_text()
            d["review"]=int(review)
            
            movieName=i.find("a",class_="unstyled articleLink")["href"][3:]
            d["movieName"]=movieName

            movieurl=i.find("a",class_="unstyled articleLink")["href"]
            m="https://www.rottentomatoes.com"+movieurl
            d["movieurl"]=m
           
            Year=i.find('a',class_="unstyled articleLink").text
            
            d["Year"]=int(Year[-5:-1])
        
        list.append(d.copy())
        if {} in list:
            list.remove({})
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
moviedata()