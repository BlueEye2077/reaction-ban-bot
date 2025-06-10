import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv("TOKEN2.env")
TOKEN=os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True
intents.reactions= True
bot = commands.Bot(command_prefix="!", intents=intents)

banned_emojis=["🖕","🇮🇱","🖕🏻","🖕🏼","🖕🏾","🖕🏿"]
ban_role_id=1325748305228988418

@bot.event
async def on_ready():
    print(f"Logged IN As {bot.user}")
    

@bot.event
async def on_reaction_add(reaction,user):
    print("reaction is triggered")

    if str(reaction.emoji) in banned_emojis:
        print("unallowed reaction is triggered")
        await reaction.remove(user)
        # await reaction.message.channel.send(f"{user} is banned from react on messages due to react with {reaction.emoji} in a message")
        ban_role=discord.utils.get(user.guild.roles,id=ban_role_id)

        embed=discord.Embed(title="You Are Banned From Reacting To Messages For Using Offensive Reactions In Hive Scans Server",color=0x171c20)
        embed.set_image(url="https://imgur.com/cnZveWM.jpg")

        await user.send(embed=embed)
        if ban_role:
            await user.add_roles(ban_role)
            print(f"{user} is banned from react on messages due to react with {reaction.emoji} in a message")


@bot.event
async def on_message(message):
    if message.content=="hello mr. x":
        await message.channel.send("...")



bot.run(TOKEN)