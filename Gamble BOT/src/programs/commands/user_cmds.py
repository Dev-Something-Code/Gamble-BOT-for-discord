from programs import points
from programs import accounts
import discord
from discord import app_commands

class Point(app_commands.Group):
    def __init__(self, *, name: str, description: str):
        super().__init__(name=name, description=description)
        pass

    @app_commands.command(name="get_user_info", description="Return User Info")    
    @app_commands.describe(user="指定のUser")
    async def get_user_info(self, interaction: discord.Interaction, user : discord.User = None):
        try:
            target = user or interaction.user
            userid = str(target.id)
            result = points.get_user_info(userid=userid)

        except Exception as e:
            embed = discord.Embed(
                title="ERROR",
                description=str(e),
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            return
        
        if result == "404":
            embed = discord.Embed(
                title="ERROR",
                description="ERROR404 User Not Found.",
                color=discord.Color.red()
            )

        else:
            user_data = f"User Name : {result['username']}\n{result['username']} has ... {result['points']} points\nWon Times : {result['win_time']} | Lost Times : {result['lose_time']} | Win Rate : {result['win_rate']}"
            embed = discord.Embed(
                title=f"Info about {result['username']}",
                description=user_data,
                color=discord.Color.green()
            )
        
        await interaction.response.send_message(embed=embed)

        return

class User(app_commands.Group):
    def __init__(self, *, name: str, description: str):
        super().__init__(name=name, description=description)
        pass

    @app_commands.command(name="create_account", description="Create your account")
    @app_commands.describe()
    async def create_account(self, interaction: discord.Interaction):
        try:
            result = accounts.create_account(userid=str(interaction.user.id),username=interaction.user.name)

        except Exception as e:
            embed = discord.Embed(
                title="ERROR",
                description=str(e),
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            return
        
        if result == "400":
            embed = discord.Embed(
                title="ERROR",
                description="ERROR400 You have already created your account.",
                color=discord.Color.red()
            )

        else:
            embed = discord.Embed(
                title="Success",
                description="You have created your account!",
                color=discord.Color.green()
            )

        await interaction.response.send_message(embed=embed)
        return