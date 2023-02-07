import discord
import custom

from discord.ext import commands
from checks.moderation import verfyadv, verfypoints
from db.moderation import adv
from functions.defs import better_time

class events(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, interaction: discord.Interaction, error):

        errorEmoji: discord.Emoji = self.bot.get_emoji(1044750438978818049)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await interaction.response.send_message(f'{errorEmoji} || {better_time(cd)}', ephemeral = True)

        # if isinstance(error, NoVote):

        #     await interaction.response.send_message(f"{errorEmoji} || {error}", ephemeral = True)
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await interaction.response.send_message(f'{errorEmoji} || Eu não tenho permissão de {error.args} para utilizar isso')

        if isinstance(error, commands.MissingPermissions):
            
            await interaction.response.send_message(f"{errorEmoji} || Você não tem permissão de {error.args} para utilizar isso", ephemeral = True)

        if isinstance(error, commands.MemberNotFound):

            await interaction.response.send_message(f'{errorEmoji} || Não encontrei esse membro')
        
        if error:

            print(error)

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        await verfyadv(self.bot,member)

        await verfypoints(self.bot,member)

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, member: discord.User):

        if adv.count_documents({ "_id": member.id}) == 1:

            adv.find_one_and_delete({"_id": member.id})

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        if message.author == self.bot.user: return
        elif message.author.bot: return
        elif message.mention_everyone: return

        if "ticket-" in message.channel.name:
            with open(f"./tickets/{message.channel.name}.txt", "a", encoding="UTF-8") as f:
                f.write(f"\n{message.author.name}: {message.content}")
    
    @commands.Cog.listener()
    async def on_ready(self):

        print("Eu entrei como {}".format(self.bot.user))
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):

        discord.ComponentType

        match interaction.to_dict()["type"]:
            case 1: return
            case 2: return
            case 3:
                match interaction.to_dict()["data"]["component_type"]:
                    case 1: return
                    case 2: await getattr(custom, f"{interaction.custom_id}")(self.bot, interaction)
                    case 3: return
                    case 4: return
                    case 5: return
            case 4: return
            case 5: return

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))