import requests
from bs4 import BeautifulSoup
import json
file=open("task1.json")
movies=json.load(file)
def group_by_year():
    d={}
    for i in movies:
        movie_list=[]
        year=i["Year"]
        if year not in d:
            for j in movies:
                if year==j["Year"]:
                    movie_list.append(j)
            d[year]=movie_list
    with open ("task2.json","w+") as file1:
        json.dump(d,file1,indent=4)
        a=json.dumps(d)
group_by_year()