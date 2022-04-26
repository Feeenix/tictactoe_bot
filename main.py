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
import ccard

# from cogs.buttons import TictactoeButtons

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
    number = ccard.visa()
    await interaction.response.send_message("Your random credit card number is: "+" ".join([ number[index:index+4] for index,substring in enumerate(number) if index%4==0])+".\n"+
    "CVV: "+str(random.randint(100,999))+"\n"+
    "Expiration date: "+str(random.randint(1,12))+"/"+str(random.randint(22,31))+"\n"+
    "Name on card: "+"".join([ random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) for i in range(0,10)])+
    " "+"".join([ random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) for i in range(0,10)]) +"\n"
    )
    return




class tic_tac_toe_game:
    
    def __init__(self,thread_channel,author,challenged,author_name,challenged_name):
        self.thread_channel = thread_channel
        self.board = [
            ["blue_square","blue_square","blue_square"],
            ["blue_square","blue_square","blue_square"],
            ["blue_square","blue_square","blue_square"],
        ]

        self.author = author
        self.challenged = challenged
        self.name_author = author_name
        self.name_challenged = challenged_name

        self.turn = "x"
        self.winner = None
        self.draw = False
        self.game_over = False
        self.game_started = False
        self.game_ended = False
    

    def make_embed(self):
        embed = nextcord.Embed(title="Tic Tac Toe",description=f"Game of {self.author} vs. {self.challenged}\n"+"\n".join([ "".join([f":{cell}:" for cell in row ]) for row in self.board ]))
        return embed
    async def send_board_buttons(self):
        buttons = TictactoeButtons(self.board)
        await self.thread_channel.send(embed=self.make_embed(),view=buttons)

class TictactoeButtons(nextcord.ui.View):
    def __init__(self, board:list=[["blue_square","blue_square","blue_square"],["blue_square","blue_square","blue_square"],["blue_square","blue_square","blue_square"],], timeout=180):
        super().__init__(timeout=timeout)
    @nextcord.ui.button(label="Button1",style=nextcord.ButtonStyle.gray)
    async def gray1_button(self,button:nextcord.ui.Button,interaction:Interaction):
        await interaction.response.edit_message(content=f"This is an edited button response!1")
    @nextcord.ui.button(label="Button2",style=nextcord.ButtonStyle.danger)
    async def gray2_button(self,button:nextcord.ui.Button,interaction:Interaction):
        await interaction.response.edit_message(content=f"This is an edited button response!2")
    @nextcord.ui.button(label="Button3",style=nextcord.ButtonStyle.success)
    async def gray3_button(self,button:nextcord.ui.Button,interaction:Interaction):
        await interaction.response.edit_message(content=f"This is an edited button response!3")


@client.slash_command(description="tic tac toe",guild_ids=testing_server_ids,force_global=True)
async def tictactoe(interaction: Interaction, challenger:nextcord.Member="AI"):
    print(interaction)
    author_name = interaction.user.nick if interaction.user.nick else interaction.user.name # str
    challenger_name = (challenger.nick if challenger.nick else challenger.name) if not type(challenger) is str else "AI" # str

    await interaction.response.send_message("you challenged "+(challenger_name),ephemeral=False,view=TictactoeButtons())
    
    thread = await interaction.channel.create_thread(name=author_name+" vs "+challenger_name,auto_archive_duration=1440,type=ChannelType(11) )
    game = tic_tac_toe_game(thread,interaction.user,challenger,author_name,challenger_name)
    await game.send_board_buttons()
    return

client.run(os.getenv("TOKEN"))