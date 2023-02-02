import os
import discord, json, NewFunctionsPYC

from discord.ext import commands
from db.economy import update_bank, bank, update_inv
from discord import slash_command, option
from economy.crafts import crafts
from economy.frutosdomar import frutos
from economy.recursos import recursos
from classes.economy.selectMenus import selectCraft

class economia(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(guild_only = True,name = 'adc_ivmcoins', description = 'Adiciona IVM coins a um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'ivmcoins', description = 'Coloque a quantidade de ivmcoins')
    async def Set(self, interaction: discord.Interaction, membro: discord.Member, ivmcoins: int):

        await update_bank(membro, + ivmcoins)

        await interaction.response.send_message(f'Foram dados {ivmcoins} IVM coins para {membro.mention}', ephemeral = True)

    @slash_command(guild_only = True,name = 'rmv_ivmcoins', description = 'Remove IVM coins de um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'ivmcoins', description = 'Coloque a quantidade de ivmcoins')
    async def Rmv(self, interaction: discord.Interaction, membro: discord.Member, ivmcoins:int):

        await update_bank(membro, - ivmcoins)

        await interaction.respond(f'Foram removidos {ivmcoins} IVM coins de {membro.mention}', ephemeral = True)
    
    @slash_command(guild_only = True, name = "inventario", description = "Mostra seu inventario")
    async def inv(self, interaction: discord.Interaction):

        try:
            os.remove("./tempinv.txt")
        except:
            pass

        e = NewFunctionsPYC.EmbedBuilder()
        e.set_title(f"Inventario de {interaction.user.name}")

        for i in frutos:
            try: 
                iv = bank.find_one({"_id": interaction.user.id})["inventario"][i["name"]]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass
        
        for i in crafts:
            try: 
                iv = bank.find_one({"_id": interaction.user.id})["inventario"][i["name"]]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass

        for i in recursos:
            try: 
                iv = bank.find_one({"_id": interaction.user.id})["inventario"][i["name"]]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass

        try:
            with open("tempinv.txt", "r", encoding = "UTF-8") as f:
                invs = f.read()
            
            e.set_description(invs)
            await interaction.response.send_message(embed = e.build(), ephemeral = True)
        except:
            await interaction.response.send_message("Você não possue inventario")

    
    @slash_command(guild_only = True, name = "craft", description = "Craft dos itens")
    @option(name = "opt", description = "Opção do que fazer", choices = ["Ver Crafts", "Craftar"])
    async def craft(self, interaction: discord.Interaction, opt: str = "Ver Crafts"):

        e = NewFunctionsPYC.EmbedBuilder()

        match opt:

            case "Ver Crafts":

                e.set_title("Ver Crafts")

                for i in crafts:
                    name = i["name"]
                    compra = i["R1"]
                    venda = i["R2"]
                    e.add_field(name = name, value = f' {compra}\n {venda}')

                await interaction.response.send_message(embed = e.build())
            
            case "Craftar":

                await interaction.response.send_message("Qual item você vai craftar", view = selectCraft(user = interaction.user.id))

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))