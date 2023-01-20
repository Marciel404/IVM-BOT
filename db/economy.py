import discord
from utils.loader import configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey'])

db = cluster["IVM"]

bank = db['bank']
#-----------------------------------------------------------------------------------------------------#
async def update_bank(membro: discord.Member, HYGCOINS: int):

    if membro is not None:

        bank.update_one({"_id": membro.id}, {"$inc": {"HYGCOINS": HYGCOINS}}, upsert = True)
#-----------------------------------------------------------------------------------------------------#