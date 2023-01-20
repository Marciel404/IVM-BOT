import discord

class ComandosStaff(discord.ui.View):
    
    @discord.ui.button(label = 'Ausencia', style = discord.ButtonStyle.blurple, custom_id = "ausencia")
    async def ausente(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = 'Cargos', style = discord.ButtonStyle.green, custom_id = "adcCargosEquipes")
    async def cargos(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = 'Ban', style = discord.ButtonStyle.red, custom_id = "banMember")
    async def ban(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = 'Advertencia', style = discord.ButtonStyle.red, custom_id = "advertência")
    async def advertência(self, button: discord.ui.Button, interaction: discord.Interaction):...

class BanButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmBan")
    async def confirmban(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def deny(self, button: discord.ui.Button, interaction: discord.Interaction):...

class KickButtons(discord.ui.View):

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmKick")
    async def confirmban(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def deny(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdvAdcButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmAdcAdv")
    async def confirmadv(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def denyadm(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdvRmvButtons(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmRmvAdv")
    async def confirmadv(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def denyadm(self, button: discord.ui.Button, interaction: discord.Interaction):...

class Ticket(discord.ui.View):
    
    @discord.ui.button(label = '🛎 Criar ticket', style = discord.ButtonStyle.blurple, custom_id = "abrirTicket")
    async def ticket(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdcCapEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmAdcCap")
    async def confirmAdcCap(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "denyAdcCap")
    async def denyAdcCap(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdcCargoEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmAdcEquipe")
    async def confirmAdcCargo(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def denyAdcCargo(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdonTicket(discord.ui.View):
    
    @discord.ui.button(label = '🔒 Fechar ticket', style = discord.ButtonStyle.blurple, custom_id = "closeTicket")
    async def closeTicket(self, button: discord.ui.Button, interaction: discord.Interaction):...

class AdonTicket2(discord.ui.View):
    
    @discord.ui.button(label = '🔓 Abrir ticket', style = discord.ButtonStyle.blurple, custom_id = "openTicket")
    async def openTicket(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '🛑 Deletar Ticket', style = discord.ButtonStyle.blurple, custom_id = "deleteTicket")
    async def deleteTicket(self, button: discord.ui.Button, interaction: discord.Interaction):...

class jumpto(discord.ui.Button):

    def __init__(self, url):

        super().__init__(

            label = 'Atalho para o ticket',

            style=discord.ButtonStyle.url,
        
            url = url
        )
    async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):...

class RmvCapEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmRmvCap")
    async def confirmRmvCap(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "denyRmvCap")
    async def deny(self, button: discord.ui.Button, interaction: discord.Interaction):...

class RmvCargoEquipes(discord.ui.View):
    
    @discord.ui.button(label = '✅', style = discord.ButtonStyle.red, custom_id = "confirmRmvEquipe")
    async def confirmRmvEquipe(self, button: discord.ui.Button, interaction: discord.Interaction):...
    @discord.ui.button(label = '❎', style = discord.ButtonStyle.red, custom_id = "deny")
    async def deny(self, button: discord.ui.Button, interaction: discord.Interaction):...