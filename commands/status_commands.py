import discord
from discord import app_commands
from utils.rcon_manager import RCONManager
from utils.embeds import create_log_embed
from arkbot import bot
from config.config_manager import ConfigManager

config = ConfigManager()

@bot.tree.command(name="status", description="Get server status")
async def status(interaction: discord.Interaction):
    rcon = RCONManager(config.RCON_HOST, config.RCON_PORT, config.RCON_PASSWORD)
    result = rcon.run_command("serverinfo")
    
    if result:
        embed = create_log_embed("Server Status", result)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Failed to retrieve server status.")
