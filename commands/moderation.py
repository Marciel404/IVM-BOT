import discord
from discord import slash_command, option
from discord.ext import commands
from classes.buttons import ComandosStaff, KickButtons, Ticket
from utils.loader import configData
from db.moderation import adv, ausen

class Moderation(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = "buttonsstaff", description = "Envia os botons de staff")
    @option(name = "channel", description = "Escolha o chat para mandar",)
    async def buttonstaff(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        
        if channel == None: channel = interaction.channel
        
        await interaction.response.send_message('Foi', ephemeral = True)
                
        await channel.send("", view = ComandosStaff())
    
    @slash_command(name = "ticketmessage", description = "Envia a mensagem do ticket")
    @option(name = 'channel', description = "Chat para enviar a mensagem")
    @option(name = "category", description = "Categoria para abrir os tickets")
    async def ticketmessage(self, interaction: discord.Interaction, channel: discord.TextChannel = None, category: discord.CategoryChannel = None):
        
        if channel == None: channel = interaction.channel
        if category == None: category = channel.category
        
        e = discord.Embed(title = 'Precisa de ajuda? Reaja a 🛎 para abrir um ticket',
        description = 'Com os tickets você pode reportar algo ou tirar alguma dúvida.',
        color = 0x4B0082)
        e.set_footer(text = f'Staff {interaction.guild.name}', icon_url = interaction.guild.icon)
        e.set_image(url = 'https://media.giphy.com/media/PfhDVTbCOsBxOMzemc/giphy.gif')
        e.set_footer(text = category.id)
        
        await channel.send(embed = e, view = Ticket())
        
        await interaction.response.send_message("Prontinho", ephemeral = True)

    @slash_command(guild_only = True,name = 'say', description = 'Envia uma mensagem em um chat')
    @option(name = 'canal', description = 'Escolha o canal que falar')
    @option(name = 'mensagem', description = 'Escreva oq deseja que eu fale')
    async def say(self, interaction: discord.Interaction, mensagem: str, canal: discord.TextChannel = None):

        if canal == None: canal = interaction.channel

        cmdl = f'''{interaction.author} usou o comando {interaction.command.name} e falou {mensagem}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

        await canal.send(mensagem)

    @slash_command(guild_only = True,name = 'editmsg', description = 'edita uma mensagem já enviada')
    @option(name = 'channel', description = 'envie o id do canal')
    @option(name = 'messageid', description = 'envie o id da mensagem')
    @option(name = 'msg', description = 'Escreva a mensagem á editar')
    @commands.has_guild_permissions(manage_channels = True)
    async def editmsg(self, interaction: discord.Interaction, msg: str, messageid: int, channel: discord.TextChannel = None ):

        if channel == None: channel = interaction.channel

        mensagem: discord.Message = await channel.fetch_message(int(messageid))

        await mensagem.edit(msg)

        cmdl = f'''{interaction.author} usou o comando {interaction.command.name} e editou a mensagem {messageid} no chat {channel.mention}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @slash_command(guild_only = True,name = 'clear', description = 'Limpa o chat')
    @option(name = 'quantidade',type = int, description = 'Escolha a quantidade de mensagens a limpar')
    @commands.has_guild_permissions(manage_channels = True)
    async def clear(self, interaction: discord.Interaction, quantidade: int = 0):

        if quantidade > 100:
            return await interaction.response.send_message('O limite maximo é de 100 mensagens')

        elif quantidade == 0:
            return await interaction.response.send_message('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 100 mensagens')

        purge = await interaction.channel.purge(limit=quantidade)

        await interaction.response.send_message(f"O chat teve {len(purge)} mensagens apagadas por {interaction.author.mention}")

        cmdl = f'''{interaction.author} usou o comando {interaction.command.name} e apagou {len(purge)} mensagens no {interaction.channel}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)
    
    @slash_command(guild_only = True,name = "embed", description = "Envia uma embed em um chat desejado")
    @option(name = "channel", description = "Escolha o chat para enviar a embed")
    @option(name = "title", description = "Escreva o titulo da embed")
    @option(name = "link_image", description = "Escolha a imagem da embed")
    @option(name = "mention", description = "Mencione um cargo para mencionar na embed")
    @option(name = "content", description = "Escreva o conteudo da embed")
    @commands.has_guild_permissions(manage_channels = True)
    async def embed(self, interaction: discord.Interaction, channel: discord.TextChannel = None, title = None, img = None, mention: discord.Role = None, *, content = None):

        if channel == None: channel = interaction.channel
        if title == None: title = ""
        if img == None: img = ""
        if content == None: content = ""
        if mention == None: mention == ""
        else: mention = mention.mention

        e = discord.Embed(title = title, description = content, colour = 0x4B0082)
        e.set_image(url = img)
        e.set_footer(text = f"{interaction.guild.name}", icon_url = interaction.guild.icon)
        await channel.send(mention, embed = e)
        await interaction.response.send_message("Enviado certinho", ephemeral = True)


        cmdl = f"""{interaction.author} usou o comando {interaction.command.name} e enviou uma embed no {channel.mention}"""
        cmdlc = self.bot.get_channel(configData["logs"]["usocomandos"])
        await cmdlc.send(cmdl)
    
    @slash_command(guild_only = True,name = 'editembed', description = 'Edita uma embed já enviada')
    @option(name = 'channel', description = 'Envie o id do canal')
    @option(name = 'embedid', description = 'Envie o id da embed')
    @option(name = 'title', description = 'Escreva o titulo da embed')
    @option(name = 'img', description = 'Escolha a imagem da embed')
    @option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @option(name = 'content', description = 'Escreva o conteudo da embed')
    @commands.has_guild_permissions(manage_channels = True)
    async def editembed(self, interaction: discord.Interaction, channel: discord.TextChannel = None, embedid: int = None, title: str = None, img: str = None, mention: discord.Role = None, content: str = None):

        if channel == None: channel: discord.TextChannel = interaction.channel
        if title == None:title = ''
        if img == None:img = ''
        if content == None: content = ''
        if mention == None: mention == ''
        else: mention = mention.mention

        mensagem = await channel.fetch_message(int(embedid))

        e = discord.Embed(title = title, description = content, colour = 0x4B0082)

        e.set_image(url = img)

        e.set_footer(text = f'{interaction.guild.name} author: {interaction.author.name}', icon_url = interaction.guild.icon)

        await mensagem.edit(mention,embed = e)

        cmdl = f'{interaction.author} usou o comando {interaction.command.name} e edtou a embed {embedid} no canal {channel.mention}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @slash_command(name = "kick", description = "Expulsa um membro")
    @option(name = "membro", description = "Escolha o membro")
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, interaction: discord.Interaction, membro: discord.Member, motivo: str = None):

        if motivo == None: motivo = "Motivo não informado"

        e1 = discord.Embed(title = "kick", description = f"Voce esta prestes a expulsar {membro.mention}")

        if membro == self.bot.user:
            return await interaction.response.send_message("Não posso expulsar a mim mesmo")

        elif  membro == interaction.author:
            return await interaction.response.send_message("Você não pode expulsar a si mesmo")

        await interaction.response.send_message(embed = e1, view = KickButtons())

        cmdl = f"""{interaction.author} usou o comando {interaction.command.name} e expulsou o {membro.name}"""

        cmdlc = self.bot.get_channel(configData["logs"]["usocomandos"])

        await cmdlc.send(cmdl)

    @slash_command(guild_only = True,name = 'veradv', description = 'Envia as advs de um membro')
    @option(name = 'membro', description = 'Escolha o membro a remover a advertencia')
    async def veradv(self, interaction: discord.Interaction, membro: discord.Member):

        myquery = { "_id": membro.id}

        if adv.count_documents(myquery) == 1:

            cmdl = f'''{interaction.author} usou o comando {interaction.command.name} e viu as advertencias de {membro.display_name}'''

            cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

            await cmdlc.send(cmdl)

            ad = adv.find_one({"_id": membro.id})

            adv1 = ad['Adv1']

            adv2 = ad['Adv2']

            adv3 = ad['Adv3']

            if adv1 == 'None':

                return await interaction.response.send_message('Esse membro não Possui advertencia', ephemeral = True)

            if adv3 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}\nAdv3: {adv3}')

                return await interaction.response.send_message(embed = e, ephemeral = True)

            if adv2 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}')

                return await interaction.response.send_message(embed = e, ephemeral = True)

            if adv1 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}')

                return await interaction.response.send_message(embed = e, ephemeral = True)

        await interaction.response.send_message('Esse membro não Possui advertencia', ephemeral = True)

        cmdl = f'''{interaction.author} usou o comando {interaction.command.name} e viu as advertencias de {membro.display_name}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @slash_command(guild_only = True,name = 'fmv', description = 'Move um membro para a sua call privada')
    @option(name = 'membro', description = 'Escolha o membro para mover para uma call')
    @option(name = 'canal', description = 'Escolha o canal para mover o membro')
    async def fmv(self, interaction: discord.Interaction, membro: discord.Member = None, canal: discord.VoiceChannel = None):

        call = self.bot.get_channel(canal.id)

        if membro.voice == None:

            return await interaction.response.send_message(f'{membro.mention} não está em um canal de voz', ephemeral = True)

        await membro.move_to(call)

        await interaction.response.send_message(f'{membro.mention} movido para {call}', ephemeral = True)

        cmdl = f'{interaction.author} usou o comando {interaction.command.name} e moveu o {membro.display_name} para o {canal.name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @slash_command(guild_only = True,name = 'fdsc', description = 'Desconecta uma pessoa da call')
    @option(name = 'membro', description = 'Escolha o membro para desconectar da call')
    async def fdsc(self, interaction: discord.Interaction, membro: discord.Member = None):

        if membro.voice == None:

            return await interaction.response.send_message(f'{membro.mention} não está em um canal de voz', ephemeral = True)

        await membro.move_to(None)

        await interaction.response.send_message(f'{membro.mention} desconectado com sucesso', ephemeral = True)

        cmdl = f'{interaction.author} usou o comando {interaction.command.name} e desconectou o {membro.display_name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @slash_command(guild_only = True,name = 'verausentes', description = 'Mostra todos os membros em estado de ausente')
    async def verausente(self, interaction: discord.Interaction):

        if ausen.find_one({"_id": 'validador'})['valor'] == 1:
            await interaction.response.send_message('Aqui está os ausentes', ephemeral = True)

            for x in ausen.find({'Ausente?': True}):
                await interaction.response.send_message(f"Nome: {x['Nome']}\nData: {x['Data']}\nMotivo: {x['Motivo']}", ephemeral = True)

        else:
            await interaction.response.send_message('Ninguem está ausente no momento', ephemeral = True)

    @slash_command(guild_only = True,name = 'verticket', description = 'Mostra as mensagens do ultimo ticket de um membro')
    @option(name = 'membro', description = 'Mostra as mensagens o ultimo ticket da pessoa')
    async def verticket(self, interaction: discord.Interaction, membro: discord.Member):

        try:
            await interaction.response.send_message(file = discord.File('./tickets/ticket-{}.txt'.format(membro.id),f'Ticket de {membro.name}.txt'), ephemeral = True)
        except:
            await interaction.response.send_message('Esse membro ainda não abriu um ticket', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(Moderation(bot))