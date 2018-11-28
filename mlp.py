
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
pprint.pprint(animes_genero)

