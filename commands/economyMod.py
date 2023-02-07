import discord
from discord.ext import commands
from discord import slash_command, option
from db.economy import update_bank, market_update, update_inv

class economyMod(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(guild_only = True,name = "adc_ivmcoins", description = "Adiciona IVM coins a um membro")
    @option(name = "membro", description = "Mencione o membro")
    @option(name = "ivmcoins", description = "Coloque a quantidade de ivmcoins")
    async def Set(self, interaction: discord.Interaction, membro: discord.Member, ivmcoins: int):

        update_bank(membro, + ivmcoins)

        await interaction.guild.get_member(485801281621852175).send(f"Foram dados {ivmcoins} IVM coins para {membro.mention} por {interaction.user}")

        await interaction.response.send_message(f"Foram dados {ivmcoins} IVM coins para {membro.mention}", ephemeral = True)

    @slash_command(guild_only = True,name = "rmv_ivmcoins", description = "Remove IVM coins de um membro")
    @option(name = "membro", description = "Mencione o membro")
    @option(name = "ivmcoins", description = "Coloque a quantidade de ivmcoins")
    async def Rmv(self, interaction: discord.Interaction, membro: discord.Member, ivmcoins:int):

        update_bank(membro, - ivmcoins)

        await interaction.guild.get_member(485801281621852175).send(f"Foram removidos {ivmcoins} IVM coins para {membro.mention} por {interaction.user}")

        await interaction.respond(f"Foram removidos {ivmcoins} IVM coins de {membro.mention}", ephemeral = True)

    @slash_command(guild_only = True, name = "update_market", description = "Atualiza um item do mercado")
    @option(name = "item", description = "Nome do item no mercado")
    @option(name = "opção", description = "Dizer se é compra ou venda", choices = ["compra", "venda"])
    @option(name = "valor", description = "Valor que vai ficar")
    async def mku(self, interaction: discord.Interaction, item: str, opção: str, valor: int):

        market_update(item, opção, valor)

        await interaction.response.send_message(f"Valor de {opção} de {item} modificado para {valor} por {interaction.user}")

        await interaction.guild.get_member(485801281621852175).send(f"Valor de {opção} de {item} modificado para {valor} por {interaction.user}")

    @slash_command(guild_only = True, name = "remove_item", description = "Remove um item de um membro")
    @option(name = "item", description = "Nome do item")
    @option(name = "qnt", description = "Quantidade a ser removida")
    @option(name = "membro", description = "Valor que vai ficar")
    async def ritem(self, interaction: discord.Interaction, item: str, qnt: int, membro: discord.Member):

        update_inv(membro, item, - qnt)

        await interaction.response.send_message(f"O item {item} foi removido de {membro} por {interaction.user} com a quantidade {qnt}", ephemeral = True)

        await interaction.guild.get_member(485801281621852175).send(f"O item {item} foi removido de {membro} por {interaction.user} com a quantidade {qnt}")
    
    @slash_command(guild_only = True, name = "give_item", description = "Adiciona um item ao membro")
    @option(name = "item", description = "Nome do item")
    @option(name = "qnt", description = "Quantidade a ser adicionada")
    @option(name = "membro", description = "Valor que vai ficar")
    async def gitem(self, interaction: discord.Interaction, item: str, qnt: int, membro: discord.Member):

        update_inv(membro, item, + qnt)

        await interaction.response.send_message(f"O item {item} foi adicionado a {membro} por {interaction.user} com a quantidade {qnt}", ephemeral = True)

        await interaction.guild.get_member(485801281621852175).send(f"O item {item} foi adicionado a {membro} por {interaction.user} com a quantidade {qnt}")

def setup(bot:commands.Bot):
    bot.add_cog(economyMod(bot))