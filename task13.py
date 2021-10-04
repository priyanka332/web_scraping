import requests
from bs4 import BeautifulSoup
import json
from task12 import scrape_movie_cast
from task1 import moviedata

movieurl="https://www.rottentomatoes.com/m/toy_story_4"
movieName="toy_story_4"
def scrape_movie_details(movieName,movieurl):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    main_div=data.find_all("li",class_="meta-row clearfix")
    dic={}
    for i in main_div:
        var=i.text
        ng=var.split(":")
        if "\nRating" in ng:
            dic["Rating"]= ng[1].replace("\n","").strip()
        elif "\nGenre" in ng:
            gen=ng[1].replace("\n                        ","").strip()
            list1=[]
            s=""
            for i in gen:
                if i==",":
                    list1.append(s)
                    s=""
                else:
                    s+=i                
            dic["Genre"]=list1
        elif "\nOriginal Language" in ng:
            dic["language"]=ng[1].replace("\n","").strip()
        elif "\nDirector" in ng:
            i=0
            list2=[]
            while i <len(ng):
                if i==0:
                    i+=1
                    continue
                list2.append(ng[i].replace("\n",""))
                i+=1
            add=""
            for s in list2:
                for s2 in s:
                    if s2==" ":
                        continue
                    else:
                        add+=s2
            list5=add.split(",")
            dic["director"]=list5
        elif "\nProducer" in ng:
            i=0
            list3=[]
            while i <len(ng):
                if i==0:
                    i+=1
                    continue
                list3.append(ng[i].replace("\n                        ","").strip())
                i+=1
            add=""
            for k in list3:
                for eachC in k:
                    if eachC==" ":
                        continue
                    else:
                        add+=eachC
            list4=add.split(",")
            dic["Producer"]=list4
        elif "\nRuntime" in ng:
            s=ng[1].replace("\n","").strip()
            h=int(s[0])*60
            i=0
            j=" "
            while i<len(s):
                if s[i]=="h" or s[i]=="m"  or s[i]==" " or i==0 or s[i]=="M":
                    i+=1
                    continue
                else:
                    j+=s[i]
                    i+=1
                h+=int(j)
            dic["Runtime"]=h
            dic["movieName"]=movieName 
            cast=scrape_movie_cast(movieName,movieurl)  
            dic["CAST & CREW"]=cast  
            return dic
scrape_movie_details("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")

movie=moviedata()
def get_movie_list_details():
    movie_list=[]
    for i in movie:
        a=i["movieurl"]
        b=scrape_movie_details(i["movieName"],a)
        movie_list.append(b)
        print(movie_list)
    with open("task13.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()