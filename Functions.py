import discord

def read_data(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

async def get_embed(bot):
    for _guild in bot.guilds:
        if _guild.name == "This is test lol":
            guild = _guild
    for _channel in guild.channels:
        if _channel.name == "инфа-типа":
            info_channel = guild.get_channel(_channel.id)
    async for last_mess in info_channel.history(limit=1):
        return last_mess

def create_embed(players):
    embed = discord.Embed(title="Заригистрированные игроки")

    embed.add_field(name="Заригистриравнные игроки:", value=players)

    return embed

def convert_list_to_dict(_list: list):
    _dict = {}
    for i in _list:
        _dict[i] = ""
    return _dict
def delete_keys(_dict: dict):
    __dict = _dict.copy()
    for i in __dict:
        __dict[i] = ""
    return __dict

def get_bool(str):
    if str.lower() == "true":
        return True
    elif str.lower() == "false":
        return False
    else:
        raise Exception(f"Unexpected argument {str}.")


def get_players():
    res = {}

    data = read_data("players")
    data = data.split("\n")

    # Parse like: nickname: {general:False}
    for line in data:
        res[line[:line.find("=")]] = {"general":get_bool(line[line.find("=") + 1:])}
    return res

def set_player(player:str, general:bool):
    data = read_data("players").split("\n")

    i = 0
    finded = False

    # Try to found player in config
    for line in data:
        lplayer = line[:line.find("=")]

        if lplayer == player:
            finded = True
            data[i] = f"{player}={general}"
        i += 1

    # If player not finded in config
    if not finded:
        data.append(f"{player}={general}")

    i = 0
    str_res = ""
    for line in data:
        if len(data) - 1 == i:
            str_res += line
        else:
            str_res += line + "\n"
        i += 1

    f = open("players", "w")
    f.write(str_res)
    f.close