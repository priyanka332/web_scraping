import requests
import os
from task1 import moviedata
movie = moviedata()
def get_movie_list_details():
    movie_list = []
    for i in movie:
        path = "/home/dell41/Desktop/web_scraping/all_files/" + i["movieName"] + ".text"
        if os.path.exists(path):
            pass
        else:
            create = open("/home/dell41/Desktop/web_scraping/all_files/" + i["movieName"] + ".text","w")
            url = requests.get(i["movieurl"])
            create1 = create.write(url.text)
            create.close()

get_movie_list_details()