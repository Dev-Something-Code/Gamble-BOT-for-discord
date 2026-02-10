from programs import gamble
import discord
from discord import app_commands
import os

class Gamble(app_commands.Group):
    def __init__(self, *, name: str, description: str):
        super().__init__(name=name, description=description)
        pass

    @app_commands.command(name="play", description="Let's Go Gambling!!")    
    @app_commands.describe(bet="賭けるお金の数")
    async def play(self, interaction: discord.Interaction, bet: int):
        file = None
        try:
            result = gamble.play(bet=bet, userid=str(interaction.user.id))
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
                
        elif result == "403":
            embed = discord.Embed(
                title="ERROR",
                description="ERROR403 Bet must be greater than 0 and less than the points you have.",
                color=discord.Color.red()
                )
                
        else:
            imgs = result['imgs']
            filename = os.path.basename(imgs)
            file = discord.File(imgs, filename=filename)
                
            embed = discord.Embed(
                title=result['title'],
                description=f"{result['txt']}\nChance : {result['probability']}",
                color=discord.Color.green()
                )
            embed.set_image(url=f"attachment://{filename}")
                
        if file:
            await interaction.response.send_message(embed=embed,file=file)
                    
        else:
            await interaction.response.send_message(embed=embed)
                
        return
            
    @app_commands.command(name="work", description="Get 1000 points")    
    @app_commands.describe()
    async def work(self, interaction: discord.Interaction):
        try:
            result = gamble.work(userid=str(interaction.user.id))
            
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
            
        elif result == "405":
            embed = discord.Embed(
                title="ERROR",
                description="ERROR405 Work is currently unavailable.Please try again after a few hours.",
                color=discord.Color.red()
                )
                
        else:
            embed = discord.Embed(
                title="Success",
                description=f"Next Work : <t:{result}:R>",
                color=discord.Color.green()
            )
            
        await interaction.response.send_message(embed=embed)
            
        return