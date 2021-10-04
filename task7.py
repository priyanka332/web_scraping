import json
with open("task5.json","r")as f:
    data=json.load(f)
def analyse_movie_director(data):
    dic1={}
    for dic in data:
        for index in dic["director"]:
            if index not in dic1:
                count=0
                for dir in data:
                    for i in dir["director"]:
                        if index==i:
                            count+=1
                dic1[index]=count
    with open("task7.json","w+") as director_data:
        json.dump(dic1,director_data,indent=4)    
analyse_movie_director(data)