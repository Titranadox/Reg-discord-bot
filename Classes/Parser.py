import discord


class Parser:
    def __init__(self, bot):
        self.bot = bot
        for _guild in bot.guilds:
            if _guild.name == "This is test lol":
                self.guild = _guild

        for _channel in _guild.channels:
            if _channel.name == "инфа-типа":
                self.info_channel = _guild.get_channel(_channel.id)

    async def get_embed_field(self):
        async for embed in self.info_channel.history(limit=1):
            return embed.embeds[0].fields[0].value

    async def get_embed(self):
        async for embed in self.info_channel.history(limit=1):
            return embed

    async def get_player_country(self, player: str):

        field_str = await self.get_embed_field()

        players_list = field_str.split(r"\n")

        for rawplayer in players_list:
            lplayer = rawplayer[player.find(".")+1:player.find("-")-1]
            if lplayer == player:
                return rawplayer[rawplayer.find("-") + 1:]

        return ""

    async def get_player_index(self, player: str):

        field_str = await self.get_embed_field()

        players_list = field_str.split(r"\n")

        i = 0
        for rawplayer in players_list:
            lplayer = rawplayer[player.find(".") + 1:player.find("-") - 1]
            if lplayer == player:
                return i
            i += 1

        return -1

    async def numerate_embed(self):
        embed = await self.get_embed_field()

        _field_str = embed.split("\n")
        i = 0
        field_str = ""
        for player in _field_str:
            _field_str[i] = str(i + 1) + _field_str[i][_field_str[i].find("."):]
            field_str += "\n" + _field_str[i]
            i += 1

        embed = await self.get_embed()
        await embed.edit(embed=self.create_embed(field_str))

    @staticmethod
    def delete_keys(_dict: dict):
        __dict = _dict.copy()
        for i in __dict:
            __dict[i] = ""
        return __dict

    @staticmethod
    def create_embed(players):
        embed = discord.Embed(title="Заригистрированные игроки")

        embed.add_field(name="Заригистриравнные игроки:", value=players)

        return embed

