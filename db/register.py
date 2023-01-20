import discord
from utils.loader import  configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey'])

db = cluster['IVM']

reg = db['registrador']

#-----------------------------------------------------------------------------------------------------#
async def addpregistro(membro: discord.Member, pontos: int):

    reg.update_one({"_id": membro.id}, {"$inc": {"registros": pontos}}, upsert = True)