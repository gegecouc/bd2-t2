from jikanpy import Jikan
from pymongo import MongoClient
from bson.son import SON
import pprint
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='bruna_braga', api_key='lmG2smF4Sf5okZa8VCQ8')

jikan = Jikan()

# inicia o cliente
client = MongoClient()
# nome do bd
db = client.t2

pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres.name", "count": {"$sum": 1}, "avg": {"$avg": "$score"}, "quantidade_votos":{"$sum", "$scored_by"}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# animes por gênero
animes_genero = list(db.anime.aggregate(pipeline))
pprint.pprint(animes_genero)

pipeline = [
    {"$unwind": "$animeography"},
    {"$group": {"_id": "$animeography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# animes por gênero (principal ou secundario)
papel_personagem_anime = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_anime)

pipeline = [
    {"$unwind": "$mangaography"},
    {"$group": {"_id": "$mangaography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# animes por gênero (principal ou secundario)
papel_personagem_manga = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_manga)

pipeline = [
    {"$unwind": "$licensors"},
    {"$group": {"_id": "$licensors.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# animes por distribuidora
animes_licensors = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_licensors)

pipeline = [
    {"$unwind": "$studios"},
    {"$group": {"_id": "$studios.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# animes por estudio
animes_studio = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_studio)

pipeline = [
    {"$unwind": "$producers"},
    {"$group": {"_id": "$producers.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
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
    {"$limit": 15}
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
    {"$limit": 15}
]
# palavras q mais aparecem na biografia do personagem
animes_word = list(db.anime.aggregate(pipeline))
# pprint.pprint(animes_word)


#GRAFICO PIZZA
labels = []
values = []
for palavra in animes_genero:
    labels.append(palavra['_id'])
    values.append(palavra['count'])

trace = go.Pie(labels=labels, values=values)
py.plot([trace], filename='basic_pie_chart')


#GRAFICO SCATTER

#grafico_media_numeroAnime_genero
labels = []
values = []
for palavra in animes_genero:
    labels.append(palavra['avg'])
    values.append(palavra['count'])

trace = go.Scatter(
    x = labels,
    y = values,
    mode = 'markers'
)
data = [trace]
py.plot(data, filename='basic-scatter')


#grafico_media_numeroVotos_numeroAnime_genero
labels = []
values = []
size=[]
for palavra in animes_genero:
    labels.append(palavra['avg'])
    values.append(palavra['count'])
    size.append(palavra['quantidade_votos'])
trace1 = go.Scatter(
    x = labels,
    y = values,
    mode='markers',
    marker=dict(
        size=size,
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]
py.plot(data, filename='scatter-plot-with-colorscale')


#GRAFICO BARRAS

