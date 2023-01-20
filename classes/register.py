import discord

from db.register import addpregistro
from utils.loader import configData

class Idade(discord.ui.View):

    @discord.ui.button(label = "🍺", style = discord.ButtonStyle.blurple, custom_id = "M18")
    async def M18(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "🍼", style = discord.ButtonStyle.blurple, custom_id = "m18")
    async def m18(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Proximo", style = discord.ButtonStyle.blurple, custom_id = "Proximo1")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass

class Genero(discord.ui.View):

    @discord.ui.button(label = "♂️", style = discord.ButtonStyle.blurple, custom_id = "GHomem")
    async def Homem(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "♀️", style = discord.ButtonStyle.blurple, custom_id = "GMulher")
    async def Mulher(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "⚧", style = discord.ButtonStyle.blurple, custom_id = "GTrans")
    async def Trans(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "🏳️‍🌈", style = discord.ButtonStyle.blurple, custom_id = "GNaoB")
    async def NãoB(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Proximo", style = discord.ButtonStyle.blurple, custom_id = "Proximo2")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass

class Sexualidade(discord.ui.View):

    @discord.ui.button(label = "👨‍❤️‍👨", style = discord.ButtonStyle.blurple, custom_id = "Hetero")
    async def Hetero(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "🏳️‍🌈", style = discord.ButtonStyle.blurple, custom_id = "Lgbt")
    async def Lgbt(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "🙎", style = discord.ButtonStyle.blurple, custom_id = "Asexual")
    async def Asexual(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Proximo", style = discord.ButtonStyle.blurple, custom_id = "Proximo3")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple, custom_id = "FinalReg")
    async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):pass

class Relacionamento(discord.ui.View):

    @discord.ui.button(label = "💍", style = discord.ButtonStyle.blurple, custom_id = "Casado")
    async def Casado(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "💌", style = discord.ButtonStyle.blurple, custom_id = "Namorrando")
    async def Namorando(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "🖖", style = discord.ButtonStyle.blurple, custom_id = "Solteiro")
    async def Solteiro(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Proximo", style = discord.ButtonStyle.blurple, custom_id = "Proximo4")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple, custom_id = "FinalReg")
    async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):pass

class Plataforma(discord.ui.View):

    @discord.ui.button(label = "💻", style = discord.ButtonStyle.blurple, custom_id = "Computador")
    async def Computador(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "📱", style = discord.ButtonStyle.blurple, custom_id = "Celular")
    async def Celular(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Proximo", style = discord.ButtonStyle.blurple, custom_id = "Proximo5")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple, custom_id = "FinalReg")
    async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):pass

class Regiao(discord.ui.View):

    @discord.ui.button(label = "Gringo", style = discord.ButtonStyle.blurple, custom_id = "RegGringo")
    async def Gringo(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Nordeste", style = discord.ButtonStyle.blurple, custom_id = "RegNordeste")
    async def Nordeste(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Norte", style = discord.ButtonStyle.blurple, custom_id = "RegNorte")
    async def Norte(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = 'Centro-Oeste', style = discord.ButtonStyle.blurple, custom_id = "RegCentroOeste")
    async def Centrooeste(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "sul", style = discord.ButtonStyle.blurple, custom_id = "RegSul")
    async def Sul(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "sudeste", style = discord.ButtonStyle.blurple, custom_id = "RegSudeste")
    async def Sudeste(self, button: discord.ui.Button, interaction: discord.Interaction):pass
    @discord.ui.button(label = "Finalizar", style = discord.ButtonStyle.blurple, custom_id = "FinalReg")
    async def Proximo(self, button: discord.ui.Button, interaction: discord.Interaction):pass


# class idade(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo

#         self.membro = membro

#         self.registrador = registrador

#         super().__init__(timeout = 300)

#     @discord.ui.button(label = '🍺', style = discord.ButtonStyle.blurple)
#     async def M18(self, button: discord.ui.Button, interaction: discord.Interaction):
    
#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['+18']) not in interaction.guild.get_member(self.membro).roles:

#             await interaction.guild.get_member(self.membro).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['+18']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['+18']) in interaction.guild.get_member(self.membro).roles:

#             await interaction.guild.get_member(self.membro).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['+18']))

#     @discord.ui.button(label = '🍼', style = discord.ButtonStyle.blurple)
#     async def m18(self, button: discord.ui.Button, interaction: discord.Interaction):
    
#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['-18']) not in interaction.guild.get_member(self.membro).roles:

#             await interaction.guild.get_member(self.membro).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['-18']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['-18']) in interaction.guild.get_member(self.membro).roles:

#             await interaction.guild.get_member(self.membro).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['idade']['-18']))

#     @discord.ui.button(label = 'Proximo', style = discord.ButtonStyle.blurple)
#     async def proximo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         e = discord.Embed(title = 'Genero',
#         description = 
# '''
# ♂️┆Menino
# ♀️┆Menina
# ⚧┆Trans
# 🏳️‍🌈┆Não Binario
# ''')

#         await interaction.response.edit_message(embed = e, view = genero(self.membro, self.registrador, self.tempo))

# class genero(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo,

#         self.membro = membro,

#         self.registrador = registrador,

#         super().__init__(timeout=300)

#     @discord.ui.button(label = '♂️', style = discord.ButtonStyle.blurple)
#     async def menino(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['macho']) not in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['macho']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['macho']) in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['macho']))

#     @discord.ui.button(label = '♀️', style = discord.ButtonStyle.blurple)
#     async def menina(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['femea']) not in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['femea']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['femea']) in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['femea']))

#     @discord.ui.button(label = '⚧', style = discord.ButtonStyle.blurple)
#     async def trans(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['trans']) not in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['trans']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['trans']) in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['trans']))

#     @discord.ui.button(label = '🏳️‍🌈', style = discord.ButtonStyle.blurple)
#     async def naob(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['naob']) not in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['naob']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['naob']) in interaction.guild.get_member(self.membro[0]).roles:

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['genero']['naob']))

#     @discord.ui.button(label = 'Proximo', style = discord.ButtonStyle.blurple)
#     async def proximo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         e = discord.Embed(title = 'Sexualidade',
#         description = 
# '''
# 👨‍❤️‍👨┆Hetero
# 🌈┆LGBTQI+
# 🙎┆Assexuado
# ''')

#         await interaction.response.edit_message(embed = e, view = sexualidade(self.membro, self.registrador, self.tempo))

#     @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple)
#     async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):

#         channel = interaction.guild.get_channel(configData['chats']['logreg'])

#         e = discord.Embed(title = 'Registro',
#         description = 
# f'''
# **Registrado:** {interaction.guild.get_member(self.membro[0]).mention}
# **Registrador:** {interaction.guild.get_member(self.registrador[0]).mention}
# **Servidor:** {interaction.guild.name}
# **Data do Registro:** {self.tempo[0]}
# ''')

#         try:

#             await interaction.guild.get_member(self.membro[0]).send(embed = e)

#             await addpregistro(interaction.guild.get_member(self.registrador[0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

#         except:

#             await addpregistro(interaction.guild.get_member(self.registrador[0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

# class sexualidade(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo,

#         self.membro = membro,

#         self.registrador = registrador,

#         super().__init__(timeout=300)

#     @discord.ui.button(label = '👨‍❤️‍👨', style = discord.ButtonStyle.blurple)
#     async def hetero(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['hetero']) not in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['hetero']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['hetero']) in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['hetero']))

#     @discord.ui.button(label = '🌈', style = discord.ButtonStyle.blurple)
#     async def lgbt(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['lgbt']) not in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['lgbt']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['lgbt']) in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['lgbt']))

#     @discord.ui.button(label = '🙎', style = discord.ButtonStyle.blurple)
#     async def asex(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['asex']) not in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['asex']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['asex']) in interaction.guild.get_member(self.membro[0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['sexual']['asex']))

#     @discord.ui.button(label = 'Proximo', style = discord.ButtonStyle.blurple)
#     async def proximo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         e = discord.Embed(title = 'Relacionamento',
#         description = 
# '''
# 💍┆Casado
# 💌┆Namorando
# 🖖┆Solteiro
# ''')

#         await interaction.response.edit_message(embed = e, view = relacionamento(self.membro, self.registrador, self.tempo))

#     @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple)
#     async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):

#         channel = interaction.guild.get_channel(configData['chats']['logreg'])

#         e = discord.Embed(title = 'Registro',
#         description = 
# f'''
# **Registrado:** {interaction.guild.get_member(self.membro[0][0]).mention}
# **Registrador:** {interaction.guild.get_member(self.registrador[0][0]).mention}
# **Servidor:** {interaction.guild.name}
# **Data do Registro:** {self.tempo[0][0]}
# ''')

#         try:

#             await interaction.guild.get_member(self.membro[0][0]).send(embed = e)

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

#         except:

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

# class relacionamento(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo,

#         self.membro = membro,

#         self.registrador = registrador,

#         super().__init__(timeout=300)

#     @discord.ui.button(label = '💍', style = discord.ButtonStyle.blurple)
#     async def casado(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['casado']) not in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['casado']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['casado']) in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['casado']))

#     @discord.ui.button(label = '💌', style = discord.ButtonStyle.blurple)
#     async def namorando(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['namo']) not in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['namo']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['namo']) in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['namo']))

#     @discord.ui.button(label = '🖖', style = discord.ButtonStyle.blurple)
#     async def solteiro(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['solte']) not in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['solte']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['solte']) in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['relacio']['solte']))

#     @discord.ui.button(label = 'Proximo', style = discord.ButtonStyle.blurple)
#     async def proximo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         e = discord.Embed(title = 'Plataforma',
#         description = 
# '''
# 💻┆Computador
# 📱┆Celular
# ''')

#         await interaction.response.edit_message(embed = e, view = plataforma(self.membro, self.registrador, self.tempo))

#     @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple)
#     async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):

#         channel = interaction.guild.get_channel(configData['chats']['logreg'])

#         e = discord.Embed(title = 'Registro',
#         description = 
# f'''
# **Registrado:** {interaction.guild.get_member(self.membro[0][0][0]).mention}
# **Registrador:** {interaction.guild.get_member(self.registrador[0][0][0]).mention}
# **Servidor:** {interaction.guild.name}
# **Data do Registro:** {self.tempo[0][0][0]}
# ''')

#         try:

#             await interaction.guild.get_member(self.membro[0][0][0]).send(embed = e)

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

#         except:

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

# class plataforma(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo

#         self.membro = membro

#         self.registrador = registrador

#         super().__init__(timeout = 300)

#     @discord.ui.button(label = '💻', style = discord.ButtonStyle.blurple)
#     async def pc(self, button: discord.ui.Button, interaction: discord.Interaction):
    
#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['pc']) not in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['pc']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['pc']) in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['pc']))

#     @discord.ui.button(label = '📱', style = discord.ButtonStyle.blurple)
#     async def cel(self, button: discord.ui.Button, interaction: discord.Interaction):
    
#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['cel']) not in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['cel']))
    
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['cel']) in interaction.guild.get_member(self.membro[0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['platform']['cel']))

#     @discord.ui.button(label = 'Proximo', style = discord.ButtonStyle.blurple)
#     async def proximo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         e = discord.Embed(title = 'Região',
#         description = 
# '''
# ❄️┆Gringo
# 🌍┆Nordeste
# 🌍┆Norte
# 🌍┆Sul
# 🌍┆Sudeste
# ''')

#         await interaction.response.edit_message(embed = e, view = regiao(self.membro, self.registrador, self.tempo))

#     @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple)
#     async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):

#         channel = interaction.guild.get_channel(configData['chats']['logreg'])

#         e = discord.Embed(title = 'Registro',
#         description = 
# f'''
# **Registrado:** {interaction.guild.get_member(self.membro[0][0][0]).mention}
# **Registrador:** {interaction.guild.get_member(self.registrador[0][0][0]).mention}
# **Servidor:** {interaction.guild.name}
# **Data do Registro:** {self.tempo[0][0][0]}
# ''')

#         try:

#             await interaction.guild.get_member(self.membro[0][0][0]).send(embed = e)

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

#         except:

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

# class regiao(discord.ui.View):

#     def __init__(self, membro, registrador, tempo):

#         self.tempo = tempo,

#         self.membro = membro,

#         self.registrador = registrador,

#         super().__init__(timeout=300)

#     @discord.ui.button(label = 'Gringo', style = discord.ButtonStyle.blurple)
#     async def gringo(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['gringo']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['gringo']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['gringo']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['gringo']))

#     @discord.ui.button(label = 'Nordeste', style = discord.ButtonStyle.blurple)
#     async def nordeste(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['nordeste']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['nordeste']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['nordeste']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['nordeste']))

#     @discord.ui.button(label = 'Norte', style = discord.ButtonStyle.blurple)
#     async def norte(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['norte']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['norte']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['norte']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['norte']))
    
#     @discord.ui.button(label = 'Centro-Oeste', style = discord.ButtonStyle.blurple)
#     async def centrooeste(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['centrooeste']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['centrooeste']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['centrooeste']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['centrooeste']))

#     @discord.ui.button(label = 'sul', style = discord.ButtonStyle.blurple)
#     async def sul(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sul']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sul']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sul']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sul']))

#     @discord.ui.button(label = 'sudeste', style = discord.ButtonStyle.blurple)
#     async def sudeste(self, button: discord.ui.Button, interaction: discord.Interaction):

#         if discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sudeste']) not in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sudeste']))
        
#         elif discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sudeste']) in interaction.guild.get_member(self.membro[0][0][0][0]).roles:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['registro']['regiao']['sudeste']))

#     @discord.ui.button(label = 'Finalizar', style = discord.ButtonStyle.blurple)
#     async def finalizar(self, button: discord.ui.Button, interaction: discord.Interaction):

#         channel = interaction.guild.get_channel(configData['chats']['logreg'])

#         e = discord.Embed(title = 'Registro',
#         description = 
# f'''
# **Registrado:** {interaction.guild.get_member(self.membro[0][0][0][0]).mention} 
# **Registrador:** {interaction.guild.get_member(self.registrador[0][0][0][0]).mention} 
# **Servidor:** {interaction.guild.name}
# **Data do Registro:** {self.tempo[0][0][0][0]}
# ''')

#         try:

#             await interaction.guild.get_member(self.membro[0][0][0][0]).send(embed = e)

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))

#         except:

#             await addpregistro(interaction.guild.get_member(self.registrador[0][0][0][0]),+1)

#             await channel.send(embed = e)

#             await interaction.response.edit_message(embed = e, view = None)

#             await interaction.guild.get_member(self.membro[0][0][0][0]).add_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['verificado']))

#             await interaction.guild.get_member(self.membro[0][0][0][0]).remove_roles(discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['naoverificado']))