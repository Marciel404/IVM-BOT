import discord
from db.economy import bank, update_inv

class selectCraft(discord.ui.View):

    def __init__(self, **kwargs):

        self.user = kwargs.get("user")

        super().__init__(timeout = 180)

    @discord.ui.select(
        placeholder = "Item",
        options = [
            discord.SelectOption(
                label = "Picareta de Ferro",
                description = "Cria a picareta de ferro",
                value = "PICFERRO"
            ),
            discord.SelectOption(
                label = "Picareta de Ouro",
                description = "Cria a picareta de ouro",
                value = "PICOURO"
            ),
            discord.SelectOption(
                label = "Picareta de diamante",
                description = "Cria a picareta de diamante",
                value = "PICDIAMANTE"
            )
        ]
    )
    async def select_callback(self, select: discord.ui.Select, interaction: discord.Interaction):

        if interaction.user.id != interaction.guild.get_member(self.user).id:
            return await interaction.response.send_message("Esse select menu não é seu", ephemeral = True)

        for i in ["madeira", "ferro", "ouro", "diamante"]:
            try:
                inv = bank.find_one({"_id": interaction.user.id})["inventario"][i]
            except Exception as error:
                update_inv(interaction.user,str(error).strip("'"),0)

        inv = bank.find_one({"_id": interaction.user.id})["inventario"]
        try:
            match select.values[0]:

                case "PICFERRO":

                    if inv["madeira"] < 1:
                        await interaction.response.send_message('Você não tem madeira suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))
                    
                    elif inv["ferro"] < 3:
                        await interaction.response.send_message('Você não tem ferro suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))

                case "PICOURO":

                    if inv["madeira"] < 1:
                        await interaction.response.send_message('Você não tem madeira suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))
                    
                    elif inv["ouro"] < 3:
                        await interaction.response.send_message('Você não tem ouro suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))

                case "PICDIAMANTE":

                    if inv["madeira"] < 1:
                        await interaction.response.send_message('Você não tem madeira suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))
                    
                    elif inv["diamante"] < 6:
                        await interaction.response.send_message('Você não tem diamante suficiente', ephemeral = True)
                        return await interaction.message.edit(view=selectCraft(user = self.user))
        except:
            await interaction.response.send_message("Iventario adicionado, selecione novamente", ephemeral = True)
            await interaction.message.edit(view=selectCraft(user = self.user))