import nextcord
from nextcord import Interaction, SlashOption, ChannelType

# class TictactoeButtons:
#     def __init__(self, ):
#         pass
class TictactoeButtons(nextcord.ui.View):
    def __init__(self, board:list=[[" "," "," "],[" "," "," "],[" "," "," "],], timeout=180):
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
# class TictactoeButtons(nextcord.ui.View):
#     def __init__(self, *, timeout=180):
#         super().__init__(timeout=timeout)
#     @nextcord.ui.button(label="Blurple Button",style=nextcord.ButtonStyle.blurple) # or .primary
#     async def blurple_button(self,button:nextcord.ui.Button,interaction:Interaction):
#         button.disabled=True
#         await interaction.response.edit_message(view=self)
#     @nextcord.ui.button(label="Gray Button",style=nextcord.ButtonStyle.gray) # or .secondary/.grey
#     async def gray_button(self,button:nextcord.ui.Button,interaction:Interaction):
#         button.disabled=True
#         await interaction.response.edit_message(view=self)
#     @nextcord.ui.button(label="Green Button",style=nextcord.ButtonStyle.green) # or .success
#     async def green_button(self,button:nextcord.ui.Button,interaction:Interaction):
#         button.disabled=True
#         await interaction.response.edit_message(view=self)
#     @nextcord.ui.button(label="Red Button",style=nextcord.ButtonStyle.red) # or .danger
#     async def red_button(self,button:nextcord.ui.Button,interaction:Interaction):
#         button.disabled=True
#         await interaction.response.edit_message(view=self)