from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

target = db.movies.find_one({'title':'매트릭스'})

db.movies.update_many({'star': target['star']},{'$set':{'star':0}})

