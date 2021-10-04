import json
from bs4 import BeautifulSoup
import requests
movieurl="https://www.rottentomatoes.com/m/toy_story_4"
movieName="toy_story_4"
def scrape_movie_cast(movieName,movieurl):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv=data.find("div",class_="castSection")
    castDiv= mainDiv.find_all("div",class_="media-body")
    dict={}
    list=[]
    for i in castDiv:
        a=i.span.text
        b=a.strip()
        z=i.find("a",class_="unstyled articleLink")
        dict1={}
        if z!= None:
            c=z["href"]
            s=""
            k=-1
            while k<=len(c[-1]):
                if c[k]=="/":
                    break
                else:
                    s+=c[k]
                k-=1
            a=s[::-1]
            # print(a)
            dict1["Name"]=b
            dict1["id"]=a
        else:
            continue
        # print(b)
        
        list.append(dict1)
        # dict["CAST & CREW"]=list
    with open("task12.json","w")as f:
        json.dump(list,f,indent=4)
    return list
scrape_movie_cast("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")