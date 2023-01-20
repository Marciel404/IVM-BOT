import discord

Intents = discord.Intents.default()
Intents.auto_moderation_configuration = False
Intents.auto_moderation_execution = False
Intents.bans = True
Intents.dm_messages = False
Intents.dm_reactions = False
Intents.dm_typing = False
Intents.emojis = True
Intents.emojis_and_stickers = True
Intents.guild_messages = True
Intents.guild_reactions = True
Intents.guild_typing = False
Intents.guilds = True
Intents.integrations = False
Intents.invites = False
Intents.members = True
Intents.message_content = True
Intents.messages = True
Intents.presences = False
Intents.reactions = True
Intents.scheduled_events = False
Intents.typing = False
Intents.voice_states = True
Intents.webhooks = True