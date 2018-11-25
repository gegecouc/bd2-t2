import json
from collections import namedtuple

import jikanpy
import requests

import time as t
from datetime import datetime

from jikanpy import Jikan
from pymongo import MongoClient

jikan = Jikan()

# inicia o cliente
client = MongoClient()
# nome do bd
db = client.t2

# nome da coleção do anime no mongo
anime = db.anime

for x in range(1, 10):  # range teste
    r = requests.get("https://api.jikan.moe/v3/anime/" + str(x))
    try:
        newAnime = jikan.anime(x)  # passar o json do anime com id x para variável
        print("Ok")
        # anime.insert_one(newAnime)  # Inserir anime na coleção do mongo db
    except jikanpy.exceptions.APIException as e:  # erro 4x na API
        print("Anime com id " + str(x) + " não existe")  # anime sem ID
    t.sleep(3)

# nome da coleção do manga no mongo
manga = db.manga

for x in range(1, 10):  # range teste
    r = requests.get("https://api.jikan.moe/v3/manga/" + str(x))
    try:
        newManga = jikan.manga(x)  # passar o json do manga com id x para variável
        print("Ok")
        # manga.insert_one(newManga)  # Inserir manga na coleção do mongo db
    except jikanpy.exceptions.APIException as e:  # erro 4x na API
        print("Manga com id " + str(x) + " não existe")  # manga sem ID
    t.sleep(3)

# nome da coleção do personagem no mongo
personagem = db.personagem

for x in range(1, 10):  # range teste
    r = requests.get("https://api.jikan.moe/v3/character/" + str(x))
    try:
        newCharacter = jikan.character(x)  # passar o json do personagem com id x para variável
        print("Ok")
        # manga.insert_one(newCharacter)  # Inserir personagem na coleção do mongo db
    except jikanpy.exceptions.APIException as e:  # erro 4x na API
        print("Personagem com id " + str(x) + " não existe")  # personagem sem ID
    t.sleep(3)

# nome da coleção da pessoa no mongo
pessoa = db.pessoa

for x in range(1, 10):  # range teste
    r = requests.get("https://api.jikan.moe/v3/person/" + str(x))
    try:
        newPessoa = jikan.person(x)  # passar o json da pessoa com id x para variável
        print("Ok")
        # pessoa.insert_one(newPessoa)  # Inserir pessoa na coleção do mongo db
    except jikanpy.exceptions.APIException as e:  # erro 4x na API
        print("Pessoa com id " + str(x) + " não existe")  # pessoa sem ID
    t.sleep(3)
