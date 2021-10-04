import json
from bs4 import BeautifulSoup
with open("task5.json","r")as f:
    data=json.load(f)
def analyse_language_and_directors(data):
    dic1={}
    for movie in data:
        for director in movie["director"]:
            dic1[director]={}
    for director in dic1:
        for dic_movie in data:
            if director in dic_movie["director"]:
                if "language" in dic_movie:
                    lan=dic_movie["language"]
                    count=0
                    dic1[director][lan]=count
                    for eachdic in data:
                        if "language" in eachdic:
                            lan2=eachdic["language"]
                            if (lan==lan2) and director in eachdic["director"]:
                                dic1[director][lan]+=1
    with open("task10.json","w+") as f:
        json.dump(dic1,f,indent=4)
analyse_language_and_directors(data)