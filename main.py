import os



import sys
import time
import datetime
import json
import requests
import urllib
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import commands
from nextcord.abc import GuildChannel
import random

from cogs.buttons import TictactoeButtons

# intents = nextcord.Intents().all()
client = commands.Bot(command_prefix="$", )
# client.remove_command("help")
# 

testing_server_ids = [814404883255132181,874954049517154315]

@client.event  
async def on_ready():
    print("client is ready")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.slash_command(description="hollow erld",guild_ids=testing_server_ids,force_global=True)
async def test(interaction: Interaction,  attachment:nextcord.Attachment=None,args:str="asdasdasd"):
    await interaction.response.send_message("ehe."+str(args),)
    print("test",args)
    return

@client.slash_command(description="your very own credit card number generator!",guild_ids=testing_server_ids,force_global=True)
async def random_credit_card(interaction: Interaction):
    number = str(random.randint(1000000000000000,9999999999999999))
    await interaction.response.send_message("Your random credit card number is: "+" ".join([ number[index:index+4] for index,substring in enumerate(number) if index%4==0])+".\n"+
    "CVV: "+str(random.randint(100,999))+"\n"+
    "Expiration date: "+str(random.randint(1,12))+"/"+str(random.randint(22,31))+"\n"+
    "Name on card: "+"".join([ random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) for i in range(0,10)])+
    " "+"".join([ random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) for i in range(0,10)]) +"\n"
    )
    return


@client.slash_command(description="tic tac toe",guild_ids=testing_server_ids,force_global=True)
async def tictactoe(interaction: Interaction, challenger:nextcord.Member="AI"):
    print(interaction)
    author_name = interaction.user.nick if interaction.user.nick else interaction.user.name # str
    challenger_name = (challenger.nick if challenger.nick else challenger.name) if not type(challenger) is str else "AI" # str

    await interaction.channel.create_thread(name=author_name+" vs "+challenger_name,auto_archive_duration )
    await interaction.response.send_message("you challenged "+(challenger_name),ephemeral=True,view=TictactoeButtons())
    return

client.run(os.getenv("TOKEN"))