import discord
import Classes.StartView
import discord_components
from Functions import *

bot = discord_components.ComponentsBot()
greetings = bot.create_group("test_bot_commands", "test_bot_command")
target_guild = "This is test lol"
target_info_channel = "инфа-типа"
guild = ""
info_channel = ""
embed_mess = ""

@bot.event
async def on_ready():
    global guild, info_channel, embed_mess

    i = 0
    for _guild in bot.guilds:
        i += 1
        if _guild.name == target_guild:
            guild_index = i
            guild = _guild
    i = 0
    for _channel in guild.channels:
        i += 1
        if _channel.name == target_info_channel:
            channel_index = i
            info_channel = guild.get_channel(_channel.id)

    last_mess = ""
    async for i in info_channel.history(limit=1): last_mess = i

    if (last_mess == "") or (last_mess.author.name != "Мяу-мяу-мяу"):
        embed_mess = await info_channel.send(embed=create_embed(""))
    else:
        embed_mess = last_mess
    print(f"Started at \nguild:{target_guild},index:{guild_index} \nChannel:{info_channel.name}, index:{channel_index}")


@greetings.command(name="test")
async def test(ctx: discord.ApplicationContext):
    embed = await get_embed(bot)
    await ctx.respond("", view=Classes.StartView.StartView(bot, embed, ctx.author), ephemeral=True)


bot.run("")
