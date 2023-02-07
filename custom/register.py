import datetime
import discord
import pytz
from discord.ext import commands
from classes.cargos.register import Genero, Sexualidade, Relacionamento, Plataforma, Regiao
from db.register import addpregistro
from utils.loader import configData

async def M18(selfbot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['idade']['+18'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def m18(selfbot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['idade']['+18'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def GHomem(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['genero']['macho'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def GMulher(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['genero']['femea'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def GTrans(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['genero']['trans'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def GNaoB(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['genero']['naob'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Hetero(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['sexual']['hetero'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Lgbt(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['sexual']['lgbt'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Asexual(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['sexual']['asex'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Casado(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['relacio']['casado'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Namorando(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['relacio']['namo'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Solteiro(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['relacio']['solte'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Computador(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['platform']['pc'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def Celular(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['platform']['cel'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegGringo(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['gringo'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegNordeste(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['nordeste'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegNorte(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['norte'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegCentroOeste(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['centrooeste'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegSul(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['sul'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)

async def RegSudeste(selfBot, Interaction: discord.Interaction):
    
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    Role = discord.utils.get(Interaction.guild.roles, id = configData['roles']['registro']['regiao']['sudeste'])
    if Role not in Member.roles: await Member.add_roles(Role)
    else: await Member.remove_roles(Role)


async def Proximo1(selfBot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Genero',
        description = 
'''
♂️┆Menino
♀️┆Menina
⚧┆Trans
🏳️‍🌈┆Não Binario
''')
    e.set_author(name = Member.id, icon_url = Member.avatar.url)
    e.set_footer(text = f"Registrador {Registrador.id}")

    await Interaction.response.edit_message(embed = e, view = Genero())

async def Proximo2(selfBot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Sexualidade',
        description = 
'''
👨‍❤️‍👨┆Hetero
🌈┆LGBTQI+
🙎┆Assexuado
''')

        
    e.set_author(name = Member.id, icon_url = Member.avatar.url)
    e.set_footer(text = f"Registrador {Registrador.id}")

    await Interaction.response.edit_message(embed = e, view = Sexualidade())

async def Proximo3(selfBot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Relacionamento',
        description = 
'''
💍┆Casado
💌┆Namorando
🖖┆Solteiro
''')
    
    e.set_author(name = Member.id, icon_url = Member.avatar.url)
    e.set_footer(text = f"Registrador {Registrador.id}")

    await Interaction.response.edit_message(embed = e, view = Relacionamento())

async def Proximo4(selfBot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Plataforma',
        description = 
'''
💻┆Computador
📱┆Celular
''')

    e.set_author(name = Member.id, icon_url = Member.avatar.url)
    e.set_footer(text = f"Registrador {Registrador.id}")

    await Interaction.response.edit_message(embed = e, view = Plataforma())

async def Proximo5(selfBot: commands.Bot, Interaction: discord.Interaction):

    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Região',
        description = 
'''
❄️┆Gringo
🌍┆Nordeste
🌍┆Norte
🌍┆Sul
🌍┆Sudeste
''')
    
    e.set_author(name = Member.id, icon_url = Member.avatar.url)
    e.set_footer(text = f"Registrador {Registrador.id}")

    await Interaction.response.edit_message(embed = e, view = Regiao())

async def FinalReg(selfBot: commands.Bot,  Interaction: discord.Interaction):

    tempo = datetime.datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y")
    channel = Interaction.guild.get_channel(configData['chats']['logreg'])
    Member = Interaction.guild.get_member(int(Interaction.message.embeds[0].author.name))
    Registrador = Interaction.guild.get_member(int(Interaction.message.embeds[0].footer.text.strip("Registrador ")))
    if Interaction.user.id != Registrador.id: await Interaction.response.send_message("Você nõa possue permissão para isso",ephemeral=True)

    e = discord.Embed(title = 'Registro',
    description = 
f'''
**Registrado:** {Member.mention}
**Registrador:** {Registrador.mention}
**Servidor:** {Interaction.guild.name}
**Data do Registro:** {tempo}
''')

    verificado = discord.utils.get(Interaction.guild.roles, id = configData['roles']['outras']['verificado'])
    naoverificado = discord.utils.get(Interaction.guild.roles, id = configData['roles']['outras']['naoverificado'])

    try:

        await Member.send(embed = e)

        await addpregistro(Registrador,+1)

        await channel.send(embed = e)

        await Interaction.response.edit_message(embed = e, view = None)

        if verificado not in Member.roles: await Member.add_roles(verificado)
        if naoverificado in Member.roles: await Member.remove_roles(naoverificado)

    except:

        await addpregistro(Registrador,+1)

        await channel.send(embed = e)

        await Interaction.response.edit_message(embed = e, view = None)

        if verificado not in Member.roles: await Member.add_roles(verificado)
        if naoverificado in Member.roles: await Member.remove_roles(naoverificado)
