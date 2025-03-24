import discord


class TestView(discord.ui.View):

    @discord.ui.button(label="Test", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.interactions.Interaction):
        await interaction.response.edit_message(content="Registred!", view=None)
