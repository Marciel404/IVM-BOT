import discord

from utils.configs import configData
from .buttonscargos import adccap, adccargo

class cargos1(discord.ui.View):

    def __init__(self, bot, timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Equipe",
        options = [
            discord.SelectOption(
                label = 'Eventos',
                description = 'Cargos da equipe de eventos',
            ),
            discord.SelectOption(
                label = 'Call',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Chat',
                description = 'Cargos da equipe de chat'
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Midia',
                description = 'Cargos da equipe de Midia'
            ),
            discord.SelectOption(
                label = 'Registro',
                description = 'Cargos da equipe de Registro'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])
        capcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])
        capchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])
        capdiv = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])
        capmidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        chefreg = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipereg']['regchefe'])

        if select.values[0] == 'Eventos':

            if capeventos in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargoevento(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

        elif select.values[0] == 'Call':

            if capcall in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargocall(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

        elif select.values[0] == 'Chat':

            if capchat in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargochat(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

        elif select.values[0] == 'Divulgação':

            if capdiv in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargodiv(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

        elif select.values[0] == 'Midia':

            if capmidia in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargomidia(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)
        
        elif select.values[0] == 'Registro':

            if chefreg in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargoreg(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

#------------------------------------------------------------------------------------------------------------#
class cargoevento(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe de eventos',
                description = 'Adiciona o cargo de chefe de eventos',
            ),
            discord.SelectOption(
                label = 'Organizador',
                description = 'Adiciona o cargo de Organizador'
            ),
            discord.SelectOption(
                label = 'Ajudante',
                description = 'Adiciona o cargo de Ajudante'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])
        org = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['apresentador'])
        ajud = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['auxiliar'])

        if select.values[0] == 'Chefe de eventos':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if capeventos in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, capeventos, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Organizador':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if org in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Org. De eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, org, interaction.user))

            self.stop()

        if select.values[0] == 'Ajudante':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if ajud in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Ajudante de Eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, ajud, interaction.user))

            self.stop()

class cargocall(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe call',
                description = 'Adiciona o cargo de Chefe call',
            ),
            discord.SelectOption(
                label = 'Staff call',
                description = 'Adiciona o cargo de staff call'
            ),
            discord.SelectOption(
                label = 'Mov. call',
                description = 'Adiciona o cargo de Mov. call'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        submod = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])
        staffcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['staffcall'])
        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['movimenta'])

        if select.values[0] == 'Chefe call':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if submod in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Chefe call')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, submod, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff call':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if staffcall in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Staff Call')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, staffcall, interaction.user))

            self.stop()

        if select.values[0] == 'Mov. call':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if movi in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Mov. call')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, movi, interaction.user))

            self.stop()

class cargochat(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe chat',
                description = 'Adiciona o cargo de Chefe chat',
            ),
            discord.SelectOption(
                label = 'Staff chat',
                description = 'Adiciona o cargo de Staff chat'
            ),
            discord.SelectOption(
                label = 'Mov. Chat',
                description = 'Adiciona o cargo de Mov. Chat'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        liderchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])
        staffchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['staffchat'])
        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['movimenta'])

        if select.values[0] == 'Chefe chat':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if liderchat in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Chefe chat')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, liderchat, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff chat':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if staffchat in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Staff Chat')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, staffchat, interaction.user))

            self.stop()

        if select.values[0] == 'Mov. Chat':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if movi in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Mov. Chat')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, movi, interaction.user))

            self.stop()

class cargodiv(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe Div',
                description = 'Adiciona o cargo de Chefe Div',
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Adiciona o cargo de divulgação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        promoters = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])
        divulgação = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['div'])

        if select.values[0] == 'Chefe Div':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if promoters in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Chefe Div')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, promoters, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Divulgação':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if divulgação in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Divulgação')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, divulgação, interaction.user))

            self.stop()

class cargomidia(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe de midia',
                description = 'Adiciona o cargo de Chefe de midia',
            ),
            discord.SelectOption(
                label = 'Equipe de midia',
                description = 'Adiciona o cargo de equipe de midia'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        chefemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])
        equipemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['equipemidia'])

        if select.values[0] == 'Chefe de midia':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if chefemidia in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Chefe Midia')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, chefemidia, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Equipe de midia':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if equipemidia in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Equipe Midia')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, equipemidia, interaction.user))

            self.stop()

class cargoreg(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Reg. Chefe',
                description = 'Adiciona o cargo de Reg. Chefe',
            ),
            discord.SelectOption(
                label = 'Registrador',
                description = 'Adiciona o cargo de Registrador'
            ),
            discord.SelectOption(
                label = 'Ajudante',
                description = 'Adiciona o cargo de Ajudante'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])
        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) 
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])
        dono = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['donos'])
        gerente = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['gerente'])
        regchefe = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipereg']['regchefe'])
        registrador = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipereg']['registrador'])
        regjunior = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipereg']['regjunior'])

        if select.values[0] == 'Reg. Chefe':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles \
            or dono in interaction.user.roles \
            or gerente in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                if regchefe in membro.roles:

                    await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                    return

                e = discord.Embed(title = 'Adicionar cargo de Reg. Chefe')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, regchefe, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Registrador':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if registrador in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Registrador')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, registrador, interaction.user))

            self.stop()

        if select.values[0] == 'Ajudante':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            if regjunior in membro.roles:

                await interaction.channel.send('Este membro já possue este cargo', delete_after = 3)

                return

            e = discord.Embed(title = 'Adicionar cargo de Reg. Junior')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, regjunior, interaction.user))

            self.stop()