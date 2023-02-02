import discord
from utils.loader import configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey'])

db = cluster["IVM"]

bank = db['bank']
#-----------------------------------------------------------------------------------------------------#
def update_bank(membro: discord.Member, IVMs: int):

    if membro is not None:

        bank.update_one({"_id": membro.id}, {"$inc": {"IVMs": IVMs}}, upsert = True)

def update_inv(member, item: str, qnt: int):

    if member is not None:

        bank.update_one(
            {"_id": member.id},
            {"$inc": {
                    f"inventario.{item}": qnt
                }
            },
        upsert = True
        )
#-----------------------------------------------------------------------------------------------------#