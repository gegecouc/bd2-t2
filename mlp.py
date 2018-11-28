
from jikanpy import Jikan
from pymongo import MongoClient
from bson.son import SON
import pprint
jikan = Jikan()

# inicia o cliente
client = MongoClient()
# nome do bd
db = client.t2

pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por gênero
animes_genero = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_genero)

pipeline = [
    {"$unwind": "$animeography"},
    {"$group": {"_id": "$animeography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por gênero (principal ou secundario)
papel_personagem_anime = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_anime)

pipeline = [
    {"$unwind": "$mangaography"},
    {"$group": {"_id": "$mangaography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por gênero (principal ou secundario)
papel_personagem_manga = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_manga)

pipeline = [
    {"$unwind": "$licensors"},
    {"$group": {"_id": "$licensors.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por distribuidora
animes_licensors = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_licensors)

pipeline = [
    {"$unwind": "$studios"},
    {"$group": {"_id": "$studios.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por estudio
animes_studio = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_studio)

pipeline = [
    {"$unwind": "$producers"},
    {"$group": {"_id": "$producers.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
# animes por produtora
animes_producer = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_producer)

pipeline = [
    {
        "$project": {
            "words": {"$split": ["$about", " "]}
        }
    },
    {
        "$unwind": "$words"
    },
    {
        "$group": {
            "_id": "$words",
            "count": {"$sum": 1}
        }
    },
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 150}
]
# palavras q mais aparecem na biografia do personagem
personagem_word = list(db.personagem.aggregate(pipeline))
# pprint.pprint(personagem_word)

pipeline = [
    {
        "$project": {
            "words": {"$split": ["$synopsis", " "]}
        }
    },
    {
        "$unwind": "$words"
    },
    {
        "$group": {
            "_id": "$words",
            "count": {"$sum": 1}
        }
    },
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 150}
]
# palavras q mais aparecem na biografia do personagem
animes_word = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_word)



