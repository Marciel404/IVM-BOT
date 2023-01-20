import discord

from discord.ext import commands
from datetime import datetime
from pytz import timezone
from classes.register import Idade

class registro(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(guild_only = True,name = 'registro', description = 'Começa o registro de um membro')
    @discord.option(name = 'membro', description = 'mencione o membro')
    async def registro(self, interaction: discord.Interaction, membro: discord.Member):

        e = discord.Embed(title = 'Idade',
        description = 
'''
🍺┆+18
🍼┆-18
''')
        e.set_footer(text = f'registrador {interaction.user.id}')
        e.set_author(name = membro.id, icon_url = membro.avatar.url)

        await interaction.respond(embed = e, view = Idade(), ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(registro(bot))

# data_e_hora_atuais = datetime.now()

# fuso_horario = timezone('America/Sao_Paulo')

# data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

# dt = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')