import os
import random
import discord
import NewFunctionsPYC

from discord.ext import commands
from db.economy import update_bank, economy, update_inv
from discord import slash_command, option
from economy.crafts import crafts
from economy.frutosdomar import on_frutos
from economy.recursos import on_recursos
from classes.economy.selectMenus import selectCraft, MercadoVer

class economia(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot
    
    @discord.slash_command(name = 'rolar', 
        description = 'Voce pode ganhar de 0 a 2000 ReCoins',
    )
    @commands.cooldown(5, 7200, commands.BucketType.user)
    async def rolar(self, interaction: discord.Interaction) -> None:

        rand: int = random.randint(0,10)

        match rand:

            case 10:

                update_bank(interaction.user, + 2000)

                await interaction.response.send_message(f'Parabens {interaction.user.name}, você ganhou 2000 ReCoins')

            case 8 | 9:

                r: int = random.randint(100,900)

                update_bank(interaction.user,r)

                await interaction.response.send_message(f'{interaction.user.name}, você ganhou {r} ReCoins')

            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7:

                r: int = random.randint(1,100)         

                update_bank(interaction.user, + r)

                await interaction.response.send_message(f'{interaction.user.name}, você ganhou {r} ReCoins')
    
    @slash_command(name = "carteira", description = "Mostra a quantidade monetaria")
    @option(name = "membro", description = "Escolha um membro")
    async def balance(self, interaction: discord.Interaction, membro: discord.Member = None):

        if membro == None: membro = interaction.user

        try:
            bal = economy.find_one({"_id": membro.id})["REcoins"]
        except Exception:
            update_bank(membro,0)
        
        bal = economy.find_one({"_id": membro.id})
        
        em = discord.Embed(title = f"{membro.name} REcoins", color = discord.Color.red())
        em.add_field(name ="Edinhos", value = bal["REcoins"])

        await interaction.response.send_message(embed = em)
    
    @slash_command(name = "transferir", description = "Transfere REcoins para outra pessoa")
    @option(name = "membro", description = "Escolha um membro")
    @option(name = "recoins", description = "Escolha a quantidade")
    async def Transferir(self, interaction: discord.Interaction, membro: discord.Member, recoins: int):
  
        try:
            economy.find_one({"_id": interaction.user.id})
        except Exception:
            update_bank(interaction.user, 0)

        bal = economy.find_one({"_id": interaction.user.id})

        if recoins > bal["REcoins"]: return await interaction.response.send_message(f"Você não tem dinheiro suficiente", ephemeral = True)
        elif recoins == 0: return await interaction.response.send_message("A quantia tem que ser maior que zero", ephemeral = True)
        elif recoins < 0: return await interaction.response.send_message(f"A quantia deve ser positiva", ephemeral = True)

        update_bank(interaction.user,- recoins)
        update_bank(membro,+ recoins)
        await interaction.response.send_message(f"Voce transferiu {recoins} REcoins para {membro.mention}")
    
    @slash_command(name = "loteria", description = "Aposta na loteria")
    @option(name = "recoins", description = "Escolha a quantidade de REcoins")
    async def loteria(self, interaction: discord.Interaction, recoins: int):
            
        try:
            economy.find_one({"_id": interaction.user.id})
        except Exception:
            update_bank(interaction.user, 0)

        bal = economy.find_one({"_id": interaction.user.id})

        if recoins > bal["REcoins"]: return await interaction.response.send_message(f"Você não tem dinheiro suficiente", ephemeral = True)
        elif recoins == 0: return await interaction.response.send_message("A quantia deve ser maior que 0", ephemeral = True)
        elif recoins < 0: return await interaction.response.send_message(f"A quantia deve ser positiva", ephemeral = True)

        final = []
        for i in range(3): final.append(random.choice([":pineapple:",":grapes:",":kiwi:"]))
        await interaction.response.defer()
        await interaction.followup.send(str(final))
        if final[0] == final[1] == final[2]:
            update_bank(interaction.user,4*recoins)
            await interaction.followup.send(f"Você ganhou {4*recoins} REcoins!!")
        else:
            update_bank(interaction.user,- recoins)
            await interaction.followup.send(f"Você perdeu {recoins} REcoins")
    
    @slash_command(name = "cara_ou_coroa_apostado")
    @option(name = "recoins", description = "Escolha a quantidade de REcoins")
    @option(name = "escolha", description = "Escolha cara ou coroa", choices = ["cara", "coroa"])
    async def Caraoucoroaap(self, interaction: discord.Interaction, recoins: int, escolha: str):

        try:
            economy.find_one({"_id": interaction.user.id})
        except Exception:
            update_bank(interaction.user, 0)
            
        bal = economy.find_one({"_id": interaction.author.id})

        if recoins > bal["REcoins"]: return await interaction.response.send_message(f"Você não tem dinheiro suficiente para apostar")
        elif recoins < 0: return await interaction.response.send_message(f"A quantia deve ser positiva")

        random1 = random.choice(["cara", "coroa"])

        if random1 == escolha:
            await interaction.response.send_message(f"Caiu {escolha}\nParabens, você ganhou {recoins*2} REcoins")
            update_bank(interaction.author, + recoins*2)
        else:
            await interaction.response.send_message(f"Caiu {random1}\nSad, você perdeu {recoins} REcoins")
            update_bank(interaction.author, - recoins)

    @slash_command(name = "recoins_top", description = "Envia os 5 mais ricos")
    async def REcoinstop(self, interaction: discord.Interaction):    

        rankings = economy.find().sort("REcoins",-1)
        i=1
        embed = discord.Embed(title = f"***Top 5 mais ricos***")
        for x in rankings:
            embed.add_field(name=f"{i}: {x['Nome']}", value=f"{x['REcoins']}", inline=False)
            if i == 5: break
            else: i += 1

        embed.set_footer(text=f"{interaction.guild}", icon_url=f"{interaction.guild.icon.url}")
        await interaction.response.send_message(embed=embed)

    @slash_command(guild_only = True, name = "inventario", description = "Mostra seu inventario")
    async def inv(self, interaction: discord.Interaction):

        try:
            os.remove("./tempinv.txt")
        except:
            pass

        e = NewFunctionsPYC.EmbedBuilder()
        e.set_title(f"Inventario de {interaction.user.name}")

        for i in await on_frutos():
            try: 
                iv = economy.find_one({"_id": interaction.user.id})["inventario"][i["name"].lower()]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass

        for i in crafts:
            try: 
                iv = economy.find_one({"_id": interaction.user.id})["inventario"][i["name"].lower()]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass

        for i in await on_recursos():
            try: 
                iv = economy.find_one({"_id": interaction.user.id})["inventario"][i["name"].lower()]
                with open("tempinv.txt", "a", encoding = "UTF-8") as f:
                    f.write(f"\n{i['name']}: {iv}")
            except Exception as error:
                pass

        try:
            with open("tempinv.txt", "r", encoding = "UTF-8") as f:
                invs = f.read()
            
            e.set_description(invs)
            await interaction.response.send_message(embed = e.build(), ephemeral = True)
        except:
            await interaction.response.send_message("Você não possue inventario", ephemeral = True)
    
    @slash_command(guild_only=True, name = "mercado", description = "Mostra o mercado")
    @option(name = "opção", description = "Escolha a opção de comprar ou vender", choices = ["comprar", "vender"])
    @option(name = "item", description = "Diga o item a comprar")
    @option(name = "quantidade", description = "Quantos itens")
    async def Shop(self, interaction: discord.Interaction, opção: str = None, item: str = None, quantidade: int = None):
        
        embed = discord.Embed(title = "Mercado", description = "Escolha a categoria")

        try:
            economy.find_one({"_id": interaction.user.id})
        except Exception:
            update_bank(interaction.user, 0)

        bal = economy.find_one({"_id": interaction.user.id})

        match opção:
            
            case None:
                await interaction.response.send_message(embed = embed, view= MercadoVer(interaction.user))

            case "comprar":

                if item == None:
                    return await interaction.response.send_message("Você precisa dizer o item a comprar")
                
                if quantidade == None:
                    return await interaction.response.send_message("Você precisa dizer a quantidade", ephemeral = True)

                item_name = item.capitalize()

                for it in await on_recursos():
                    if it["name"] == item_name:
                        price = it["compra"]
                        break
                
                for it in await on_frutos():
                    if it["name"] == item_name:
                        price = it["compra"]
                        break

                cost = price*quantidade

                if bal["REcoins"] < cost:
                    await interaction.response.send_message("Você não tem ReCoins suficientes")
                else:
                
                    q = "unidade"
                    if quantidade > 1:
                        q = "unidades"

                    await interaction.response.send_message(f"Você comprou {quantidade} {q} de {item} por {cost} ReCoins")
                    update_bank(interaction.author, - cost)
                    update_inv(interaction.author, item_name, quantidade)

            case "vender":

                if item == None:
                    return await interaction.response.send_message("Você precisa dizer o item a vender", ephemeral = True)
                
                if quantidade == None:
                    return await interaction.response.send_message("Você precisa dizer a quantidade", ephemeral = True)

                item_name = item.capitalize()

                for it in await on_recursos():
                    if it["name"] == item_name:
                        price = it["venda"]
                        break
                
                for it in await on_frutos():
                    if it["name"] == item_name:
                        price = it["venda"]
                        break

                cost = price*quantidade

                if bal["inventario"][item.lower()] < 1:
                    await interaction.response.send_message("Você não tem esse item para vender")
                else:

                    q = "unidade"
                    if quantidade > 1:
                        q = "unidades"

                    await interaction.response.send_message(f"Você vendeu {quantidade} {q} de {item} por {cost} REcoins")
                    update_bank(interaction.author, + cost)
                    update_inv(interaction.author, item_name, - quantidade)
    
    @slash_command(guild_only = True, name = "craft", description = "Craft dos itens")
    @option(name = "opt", description = "Opção do que fazer", choices = ["Ver Crafts", "Craftar"])
    async def craft(self, interaction: discord.Interaction, opt: str = "Ver Crafts"):

        e = NewFunctionsPYC.EmbedBuilder()

        match opt:

            case "Ver Crafts":

                e.set_title("Ver Crafts")

                for i in crafts:
                    name = i["name"]
                    compra = i["R1"]
                    venda = i["R2"]
                    e.add_field(name = name, value = f" {compra}\n {venda}")

                await interaction.response.send_message(embed = e.build())
            
            case "Craftar":

                await interaction.response.send_message("Qual item você vai craftar", view = selectCraft(user = interaction.user.id))

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))