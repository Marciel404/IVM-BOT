import discord
import custom

from discord.ext import commands
from utils.loader import configData
from datetime import datetime
from pytz import timezone
from checks.moderation import verfyadv, verfypoints
from db.moderation import adv

class events(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

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

            with open(f"./tickets/{message.channel.name}.txt", "a") as f:

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