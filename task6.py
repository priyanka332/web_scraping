import json
from bs4 import BeautifulSoup
with open ("task5.json","r")as f:
    data=json.load(f)
def analyse_movie_language(data):
    dict1={}
    for dic in data:
        if "language" in dic:
            language=dic["language"]
            if language not in dict1:
                language=dic["language"]
                dict1[language]=1
            else:
                dict1[language]+=1
        else:
            continue
    with open("task6.json","w")as f:
        json.dump(dict1,f,indent=4)
analyse_movie_language(data)