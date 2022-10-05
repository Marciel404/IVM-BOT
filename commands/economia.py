import discord

from discord.ext import commands
from db.economy import update_bank

class economia(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @discord.slash_command(guild_only = True,name = 'adc_ivmcoins', description = 'Adiciona ivm coins a um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'ivmcoins', description = 'Coloque a quantidade de ivmcoins')
    async def Set(self,ctx, membro: discord.Member, ivmcoins: int):

        await update_bank(membro, + ivmcoins)

        await ctx.respond(f'Foram dados {ivmcoins} ivm coins para {membro.mention}', ephemeral = True)

    @discord.slash_command(guild_only = True,name = 'rmv_ivmcoins', description = 'Remove ivm coins a um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'ivmcoins', description = 'Coloque a quantidade de ivmcoins')
    async def Rmv(self,ctx, membro: discord.Member, ivmcoins:int):

        await update_bank(membro, - ivmcoins)

        await ctx.respond(f'Foram removidos {ivmcoins} ivm coins de {membro.mention}', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))