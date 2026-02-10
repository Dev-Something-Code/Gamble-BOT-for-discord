import discord
from discord.ext import commands
from programs.commands import gamble_cmds, user_cmds

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.tree.add_command(gamble_cmds.Gamble(name="gamble", description="Gamble Cmds"))
bot.tree.add_command(user_cmds.User(name="user", description="User Cmds"))
bot.tree.add_command(user_cmds.Point(name="points", description="Points Cmds"))

@bot.event
async def on_ready():
    print(f"Susscess to ready | Bot Name : {bot.user}")
    await bot.tree.sync()

bot.run("YOURE TOKEN HERE")