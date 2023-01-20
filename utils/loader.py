import os
import json
from discord.ext.commands import Bot as BotBase
from .intents import Intents

with open("utils/config.json", "r" , encoding="UTF-8") as config:
    configData = json.load(config)

class client(BotBase):

    def __init__(self):
        super().__init__(
            command_prefix = "IVM!",
            help_command = None,
            intents = Intents,
        )

    def __load_cogs__(self):

        for commands in os.listdir("./commands"):
            if commands.endswith(".py") and not commands.startswith("__"):
                self.load_extension("commands.{}".format(commands[:-3]))
        
        for plugins in os.listdir("./plugins"):
            if plugins.endswith(".py") and not plugins.startswith("__"):
                self.load_extension("plugins.{}".format(plugins[:-3]))

    def __run__(self):
        self.__load_cogs__()
        self.run(configData["token"])