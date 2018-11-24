import jikanpy
import requests

import time as t
from datetime import datetime

from jikanpy import Jikan
from pymongo import MongoClient

# inicia o cliente
client = MongoClient()
# nome do bd
db = client.t2
# nome da coleção
anime = db.anime

jikan = Jikan()

for x in range(1, 10): # range teste
    r = requests.get("https://api.jikan.moe/v3/anime/" + str(x))
    try:
        newAnime = jikan.anime(x)  # passar o json do anime com id x para variável
        print("Ok")
        # anime.insert_one(newAnime)  # Inserir anime na coleção do mongo db
    except jikanpy.exceptions.APIException as e: #erro 4x na API
        print("Anime com id " + str(x) + " não existe")  # anime sem ID
    t.sleep(3)