import requests
import os
import time
import random
from task1 import moviedata
movie = moviedata()
def get_movie_list_details():
    movie_list = []
    for i in movie:
        path = "/home/dell41/Desktop/web_scraping/All_file/" + i["movieName"] + ".text"
        random_sleep = random.randint(1,5)
        if os.path.exists(path):
            pass
        else:
            time.sleep(random_sleep)
            create = open("/home/dell41/Desktop/web_scraping/All_file/" + i["movieName"] + ".text","w")
            url = requests.get(i["movieurl"])
            create1 = create.write(url.text)
            create.close()
get_movie_list_details()