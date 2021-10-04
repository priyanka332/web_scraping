import requests
from bs4 import BeautifulSoup
import json
file=open("task1.json")
movies=json.load(file)
decades={"1937":[],"1947":[],"1957":[],"1967":[],"1977":[],"1987":[],"1997":[],"2007":[],"2017":[],"2027":[]}
def group_by_decade(movies):
    for index in movies:
        if index["Year"]>=1937 and index["Year"]<1947:
            decades["1937"].append(index)
        elif index["Year"]>=1947 and index["Year"]<1957:
            decades["1947"].append(index)    
        elif index["Year"]>=1957 and index["Year"]<1967:
            decades["1957"].append(index)
        elif index["Year"]>=1967 and index["Year"]<1977:
            decades["1967"].append(index)
        elif index["Year"]>=1977 and index["Year"]<1987:
            decades["1977"].append(index)
        elif index["Year"]>=1987 and index["Year"]<1997:
            decades["1987"].append(index)
        elif index["Year"]>=1997 and index["Year"]<2007:
            decades["1997"].append(index)
        elif index["Year"]>=2007 and index["Year"]<2017:
            decades["2007"].append(index)
        elif index["Year"]>=2017 and index["Year"]<2027:
            decades["2017"].append(index)
        with open("task3.json","w+") as file3:
            json.dump(decades,file3,indent=4)
            a=json.dumps(decades)
group_by_decade(movies)