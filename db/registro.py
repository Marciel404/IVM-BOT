from utils.configs import  configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey'])

db = cluster['IVM']

reg = db['registrador']

#-----------------------------------------------------------------------------------------------------#
async def addpregistro(membro, pontos):

    reg.update_one({"_id": membro.id}, {"$inc": {"registros": pontos}}, upsert = True)