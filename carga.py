import requests

import time as t
from datetime import datetime
from jikanpy import Jikan
from pymongo import MongoClient

#inicia o cliente
client = MongoClient()
# nome do bd
db = client.t2
# nome da coleção
anime = db.anime

jikan = Jikan()
cont = 0
for x in range(1, 20):
    r = requests.get("https://api.jikan.moe/v3/anime/"+str(x))

    if(r.status_code==200):
        print("Anime com id: "+str(x))
        newAnime = jikan.anime(x)
        #result = anime.insert_one(newAnime)
    else:
        print("Erro")
    t.sleep( 3 )