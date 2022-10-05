import discord

from .configs import configData
from db.mod import mod, msgcmdstf, msgtckid, tick, adv
from db.evento import points
from classes.ticket import ticket, adonticket, adonticket2
from classes.buttonsstaff import cmdstf

async def bottonstaffloader(self):

    guild = self.get_guild(configData["guild"])

    channel = self.get_channel(configData['chats']['cmdstf'])

    try:

        mensagem = await channel.fetch_message(mod.find_one({'_id': guild.id})['msgcmdstf'])

        await mensagem.edit(view = cmdstf(self))
    
    except:

        await channel.purge(limit=1)

        msg = await channel.send(view = cmdstf(self))

        await msgcmdstf(msg.id, guild)
#-----------------------------------------------------------------------------------------------------#
async def ticketloader(self):

    guild = self.get_guild(configData["guild"])

    e = discord.Embed(

    title = 'Precisa de ajuda? Reaja a 📩 para abrir um ticket',

    description = 'Com os tickets você pode reportar algo ou tirar alguma dúvida.',

    color = 0x4B0082)

    e.set_footer(text = 'Staff IVM', icon_url = guild.icon)

    e.set_image(url = 'https://media.giphy.com/media/PfhDVTbCOsBxOMzemc/giphy.gif')

    channel = self.get_channel(configData['chats']['ticket'])  

    try:

        mensagem = await channel.fetch_message(mod.find_one({'_id': guild.id})['msgtck'])

        await mensagem.edit(view = ticket())
    
    except:

        await channel.purge(limit=1)

        msg = await channel.send(embed = e, view = ticket())

        await msgtckid(msg.id, guild)
#-----------------------------------------------------------------------------------------------------#
async def verfyadv(self, member):

    role1 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv1'])

    role2 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv2'])

    role3 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv3'])

    if adv.count_documents({ "_id": member.id}) == 1:

        ad = adv.find_one({"_id": member.id})

        adv1 = ad['Adv1']

        adv2 = ad['Adv2']

        adv3 = ad['Adv3']

        if adv3 != 'None':

            await  member.add_roles(role1, role2, role3)

            return

        if adv2 != 'None':

            await  member.add_roles(role1, role2)

            return

        if adv1 != 'None':

            await  member.add_roles(role1)

            return
#-----------------------------------------------------------------------------------------------------#
async def verfypoints(self, member):

    if points.count_documents({ "_id": member.id}) == 1:

        p = points.find_one({"_id": member.id})

        if discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆') in member.guild.roles:

            await member.add_roles(discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆'))
#-----------------------------------------------------------------------------------------------------#
async def verifyticket(self):

    if tick.find_one({"_id": 'validador'})['valor'] == 1:

        for x in tick.find({'aberto?': True}):

            channel = discord.utils.get(self.get_guild(configData['guild']).channels, name = f'ticket-{x["_id"]}')

            msg = await channel.fetch_message(x['msgid'])

            await msg.edit(view = adonticket(self.get_user(x["_id"])))

        for x in tick.find({'fechado?': True}):

            channel = discord.utils.get(self.get_guild(configData['guild']).channels, name = f'ticket-{x["_id"]}')

            msg = await channel.fetch_message(x['msgid'])

            await msg.edit(view = adonticket2(self.get_user(x["_id"])))