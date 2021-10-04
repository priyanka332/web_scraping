import json
from bs4 import BeautifulSoup
from task1 import moviedata
from task4 import scrape_movie_details

movie=moviedata()
def get_movie_list_details():
    movie_list=[]
    for i in movie:
        a=i["movieurl"]
        b=scrape_movie_details(i["movieName"],a)
        movie_list.append(b)
        # print(movie_list)
    with open("task5.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()