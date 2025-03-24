import discord
from Classes.Views.AsiaView import AsiaView
from Classes.Views.SouthAmericaView import SouthAmericaView
from Classes.Views.EuropaView import EuropaView
from Classes.Views.NorthAmericaView import NorthAmericaView
from Classes.Views.CentralAmericaView import CentralAmericaView
from Classes.Views.CaribbeanRegionView import CaribbeanRegionView
from Classes.Views.AfricaView import AfricaView
from Classes.Views.OceaniaView import OceaniaView
from Functions import *

World_parts = [discord.SelectOption(label="Азия"),
               discord.SelectOption(label="Европа"),
               discord.SelectOption(label="Африка"),
               discord.SelectOption(label="Южная Америка"),
               discord.SelectOption(label="Северная Америка"),
               discord.SelectOption(label="Центральная Америка"),
               discord.SelectOption(label="Океания"),
               discord.SelectOption(label="Карибский регион")]


class StartView(discord.ui.View):

    def __init__(self, bot, embed_info, author):
        super().__init__()
        self.bot = bot
        self.author = author
        self.embed = embed_info
        for _guild in bot.guilds:
            if _guild.name == "This is test lol":
                self.guild = _guild

        players = get_players()
        if author.display_name in players:
            if players[author.display_name]["general"]:
                label = "Разрешить другим быть вашими генералами: Да"
                style = discord.ButtonStyle.green
            else:
                label = "Разрешить другим быть вашими генералами: Нет"
                style = discord.ButtonStyle.red
        else:
            label = "Разрешить другим быть вашими генералами: Нет"
            style = discord.ButtonStyle.red

        self.add_item(discord.ui.Button(label=label, style=style))
        self.children[-1].callback = self.change_general

        # TODO: accurate nickname check. For example, if in list be "doxin" and "dox", it's find player
        # TODO: if create new embed get error
        finded = self.embed.embeds[0].fields[0].value.find(self.author.display_name) != -1

        if finded:
            # TODO: do like: "Выйти из катки: Россия"
            self.add_item(discord.ui.Button(label="Выйти из катки", style=discord.ButtonStyle.primary, row=1))

            self.children[-1].callback = self.exit_command

    @discord.ui.select(placeholder="Ыыыыыы", options=World_parts)
    async def select_callback(self, select, interaction: discord.Interaction):
        embed_info = await get_embed(self.bot)
        author = interaction.user

        # Give up, I don't know "switch"
        if select.values[0] == "Азия":
            await interaction.response.edit_message(view=AsiaView(self.bot, embed_info, author))
        elif select.values[0] == "Европа":
            await interaction.response.edit_message(view=EuropaView(self.bot, embed_info, author))
        elif select.values[0] == "Африка":
            await interaction.response.edit_message(view=AfricaView(self.bot, embed_info, author))
        elif select.values[0] == "Южная Америка":
            await interaction.response.edit_message(view=SouthAmericaView(self.bot, embed_info, author))
        elif select.values[0] == "Северная Америка":
            await interaction.response.edit_message(view=NorthAmericaView(self.bot, embed_info, author))
        elif select.values[0] == "Океания":
            await interaction.response.edit_message(view=OceaniaView(self.bot, embed_info, author))
        elif select.values[0] == "Центральная Америка":
            await interaction.response.edit_message(view=CentralAmericaView(self.bot, embed_info, author))
        elif select.values[0] == "Карибский регион":
            await interaction.response.edit_message(view=CaribbeanRegionView(self.bot, embed_info, author))

    async def exit_command(self, interaction: discord.Interaction):
        # Get embed
        embed_mess = await get_embed(self.bot)

        # Just need, its have too bad optimization
        # TODO: Fix this shit
        await interaction.response.edit_message(content="Вы теперь не учасвуйте", view=None)
        field_str = embed_mess.embeds[0].fields[0].value

        # If player can leave from game
        if field_str.find(interaction.user.display_name) != -1:
            _field_str = field_str.split("\n")

            # Delete player
            i = 0
            for player in _field_str:
                _player = player[player.find(".") + 1:player.find("-")]
                if _player.find(interaction.user.display_name) != -1:
                    _field_str.pop(i)
                i += 1

            # TODO: add numerate from parser
            # Numerate players
            i = 0
            field_str = ""
            for player in _field_str:
                _field_str[i] = str(i + 1) + _field_str[i][_field_str[i].find("."):]
                field_str += "\n" + _field_str[i]
                i += 1

            await self.embed.edit(embed=create_embed(field_str))

    async def change_general(self, interaction: discord.Interaction):
        players = get_players()
        if self.author.display_name in players:
            set_player(self.author.display_name, not players[self.author.display_name]["general"])
        else:
            set_player(self.author.display_name, True)

        embed = await get_embed(self.bot)
        await interaction.response.edit_message(view=StartView(self.bot, embed, self.author))