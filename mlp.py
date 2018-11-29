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


#--------------------anime-----------------


pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres.name", "count": {"$sum": 1}, "avg": {"$avg": "$score"}, "quantidade_votos":{"$sum": "$scored_by"}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}

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




#------------------ manga -------------------------

pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres.name", "count": {"$sum": 1}, "avg": {"$avg": "$score"}, "quantidade_votos":{"$sum": "$scored_by"}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}

]
# mangas por gênero
mangas_genero = list(db.manga.aggregate(pipeline))
pprint.pprint(mangas_genero)


pipeline = [
    {"$unwind": "$mangaography"},
    {"$group": {"_id": "$mangaography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas por gênero (principal ou secundario)
papel_personagem_manga = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_manga)

pipeline = [
    {"$unwind": "$authors"},
    {"$group": {"_id": "$authors.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas por autores
mangas_authors = list(db.manga.aggregate(pipeline))


pipeline = [
    {"$unwind": "$serializations"},
    {"$group": {"_id": "$serializations.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas serializacoes
mangas_serializacoes = list(db.manga.aggregate(pipeline))


#------------------ pessoas -------------------------


pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres.name", "count": {"$sum": 1}, "avg": {"$avg": "$score"}, "quantidade_votos":{"$sum": "$scored_by"}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}

]
# mangas por gênero
mangas_genero = list(db.manga.aggregate(pipeline))
pprint.pprint(mangas_genero)


pipeline = [
    {"$unwind": "$mangaography"},
    {"$group": {"_id": "$mangaography.role", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas por gênero (principal ou secundario)
papel_personagem_manga = list(db.personagem.aggregate(pipeline))
# pprint.pprint(papel_personagem_manga)

pipeline = [
    {"$unwind": "$authors"},
    {"$group": {"_id": "$authors.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas por autores
mangas_authors = list(db.manga.aggregate(pipeline))


pipeline = [
    {"$unwind": "$serializations"},
    {"$group": {"_id": "$serializations.name", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])},
    {"$limit": 10}
]
# mangas serializacoes
mangas_serializacoes = list(db.manga.aggregate(pipeline))


#------------------ personagens ---------------------








#------------------------------------------GRAFICO PIZZA-------------------------------------------


#--------- anime ---------
labels = []
values = []
for x in range (0, 15):
    labels.append(animes_genero[x]['_id'])
    values.append(animes_genero[x]['count'])

trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename='anime-genero', auto_open=False)


#--------- manga ----------
labels = []
values = []
for x in range (0, 15):
    labels.append(mangas_genero[x]['_id'])
    values.append(mangas_genero[x]['count'])

trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename='manga-genero', auto_open=False)



#-----------------------------------------GRAFICO SCATTER-----------------------------------------
#--------- animes ----------

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
plotly.offline.plot(data, filename='media-anime',auto_open=False)


#grafico_media_numeroVotos_numeroAnime_genero
labels = []
values = []
size=[]
ids=[]
for palavra in animes_genero:
    ids.append(palavra['_id'])
    labels.append(palavra['avg'])
    values.append(palavra['count'])
    size.append(palavra['quantidade_votos'])
trace1 = go.Scatter(
    x=labels,
    y=values,
    hovertext=ids,
    mode='markers',
    marker=dict(
        size=16,
        colorscale='Viridis',
        color = size,
        showscale=True,
        colorbar=dict(
            title='Quantidade de votos',
            titleside='top'
        )
    )
)
data = [trace1]

layout = dict(xaxis=dict(title="Média das notas"),
              yaxis=dict(title="Quantidade de animes"),
         )

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='media-anime-votos',auto_open=False)


#--------- mangas ----------

#grafico_media_numeroMangas_genero
labels = []
values = []
for palavra in mangas_genero:
    labels.append(palavra['avg'])
    values.append(palavra['count'])

trace = go.Scatter(
    x = labels,
    y = values,
    mode = 'markers'
)
data = [trace]
plotly.offline.plot(data, filename='media-manga',auto_open=False)


#grafico_media_numeroVotos_numeroMangas_genero
labels = []
values = []
size=[]
ids=[]
for palavra in mangas_genero:
    ids.append(palavra['_id'])
    labels.append(palavra['avg'])
    values.append(palavra['count'])
    size.append(palavra['quantidade_votos'])
trace1 = go.Scatter(
    x=labels,
    y=values,
    hovertext=ids,
    mode='markers',
    marker=dict(
        size=16,
        colorscale='Viridis',
        color = size,
        showscale=True,
        colorbar=dict(
            title='Quantidade de votos',
            titleside='top'
        )
    )
)
data = [trace1]

layout = dict(xaxis=dict(title="Média das notas"),
              yaxis=dict(title="Quantidade de mangás"),
         )

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='media-manga-votos',auto_open=False)

#----------------------------------------GRAFICO PONTOS-----------------------------------

#-------Pessoas---------

# trace1 = {"x": [72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112],
#           "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
#                 "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
#                 "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
#           "marker": {"color": "pink", "size": 12},
#           "mode": "markers",
#           "name": "Women",
#           "type": "scatter"
# }
#
# trace2 = {"x": [92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151, 152, 165],
#           "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
#                 "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
#                 "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
#           "marker": {"color": "blue", "size": 12},
#           "mode": "markers",
#           "name": "Men",
#           "type": "scatter",
# }
#
# data = [trace1, trace2]
# layout = {"title": "Gender Earnings Disparity",
#           "xaxis": {"title": "Annual Salary (in thousands)", },
#           "yaxis": {"title": "School"}}
#
# fig = go.Figure(data=data, layout=layout)
# py.iplot(fig, filenmae='basic_dot-plot')
