import discord
from math import floor
import Classes.StartView
from Classes.Parser import Parser


class BaseCountriesView(discord.ui.View):
    def __init__(self, bot, embed_mess, author, countries):
        super().__init__(timeout=None)
        self.countries = countries
        self.embed_mess = embed_mess
        self.author = author
        self.bot = bot
        self.author = ""
        parser = Parser(self.bot)

        for _guild in bot.guilds:
            if _guild.name == "This is test lol":
                self.guild = _guild

        back_button_placed = False
        back_button_row = floor(len(countries) / 5)

        field_str = embed_mess.embeds[0].fields[0].value

        _field_str = field_str.split(r"\n")
        countries_dict = parser.delete_keys(self.countries)

        # Parse like: Country:player
        for country in countries_dict:
            for player in _field_str:
                if player.find(country) != -1:
                    if player.find(",") != -1:
                        countries_dict[country] = player[player.find(".") + 1:player.find(",")] + player[player.find(",") + 1:player.find("-")]
                    else:
                        countries_dict[country] = player[player.find(".") + 1:player.find("-")]
                    print(countries_dict[country])

        i = 0
        row = 0
        country = ""
        for country in self.countries:
            i += 1

            if i == 6:
                row += 1
                i = 1
            if row == back_button_row:
                back_button_placed = True
                self.add_item(discord.ui.Button(label="Назад",
                                                style=discord.ButtonStyle.primary,
                                                row=back_button_row,
                                                custom_id="back_button"))
                self.children[-1].callback = self.callback_back_button
                back_button_row = -1

            if countries_dict[country] != "":
                label = f"{country}-{countries_dict[country]}"
                if countries_dict[country] == author.display_name:
                    style = discord.ButtonStyle.green
                else:
                    style = discord.ButtonStyle.red
            else:
                label = country
                style = discord.ButtonStyle.primary
            self.add_item(discord.ui.Button(label=label,
                                            style=style,
                                            emoji=self.countries[country],
                                            row=row,
                                            custom_id=country))
            self.children[-1].callback = self.callback_buttons
        if not back_button_placed:
            self.add_item(discord.ui.Button(label="Назад",
                                            style=discord.ButtonStyle.primary,
                                            row=back_button_row,
                                            custom_id="back_button"))
            self.children[-1].callback = self.callback_back_button

    async def callback_buttons(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"Зарегистрирован как {interaction.data["custom_id"]}!", view=None)
        parser = Parser(self.bot)

        field_str = await parser.get_embed_field()


        if field_str.find(interaction.user.display_name) != -1:
            _field_str = field_str.split(r"\n")

            for player in _field_str:
                if player.find(interaction.user.display_name) != -1:
                    _field_str = player[3 + len(interaction.user.display_name):]
                    field_str = field_str.replace(_field_str, interaction.data["custom_id"])
        else:
            field_str += f"\n{1}.{interaction.user.display_name}-{interaction.data["custom_id"]}"


        embed = await parser.get_embed()
        await embed.edit(embed=parser.create_embed(field_str))
        # TODO: At good, do numerate on string, not in embed
        await parser.numerate_embed()

    async def callback_back_button(self, interaction: discord.Interaction):
        parser = Parser(self.bot)
        await interaction.response.edit_message(view=Classes.StartView.StartView(self.bot, await parser.get_embed(), interaction.user))