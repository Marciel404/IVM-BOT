import discord
from utils.loader import  configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData["mongokey"])

db = cluster["IVM"]
adv = db["adv"]
mod = db["mod"]
ausen = db["ausente"]
#-----------------------------------------------------------------------------------------------------#
async def adcadvdb(membro: discord.Member, qnt, motivo):

    adv.update_one({"_id": membro.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)

async def rmvadvdb(membro: discord.Member, qnt, motivo):

    adv.update_one({"_id": membro.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)
#-----------------------------------------------------------------------------------------------------#
async def ausendb(membro: discord.Member, motivo, data):

    ausen.update_one({"_id": membro.id}, {"$set": {f"Nome": membro.name, f"Motivo": motivo, f"Data": data, "Ausente?": True}}, upsert = True)

    if ausen.find_one({"_id": "validador"})["valor"] == 0:

        ausen.update_one({"_id": "validador"}, {"$set": {f"valor": 1}}, upsert = True)

async def desausendb(membro: discord.Member):

    ausen.update_one({"_id": membro.id}, {"$set": {f"Nome": membro.name, f"Motivo": "None", f"Data": "None", "Ausente?": False}}, upsert = True)

    if ausen.count_documents({"Ausente?": True}) == 0:

        ausen.update_one({"_id": "validador"}, {"$set": {f"valor": 0}}, upsert = True)
#-----------------------------------------------------------------------------------------------------#