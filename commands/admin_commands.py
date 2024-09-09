import discord
from discord import app_commands
from utils.embeds import create_log_embed
from utils.mongo_manager import MongoManager
from utils.rcon_manager import RCONManager
from arkbot import bot
from config.config_manager import ConfigManager

# Initialize MongoDB and config managers
mongo_manager = MongoManager()
config = ConfigManager()

@bot.tree.command(name="admin", description="Run admin commands")
@app_commands.describe(action="Action to perform on the server (restart, save, etc.)")
async def admin_command(interaction: discord.Interaction, action: str):
    rcon = RCONManager(config.RCON_HOST, config.RCON_PORT, config.RCON_PASSWORD)
    
    log_channel_id = mongo_manager.get_channel("log")
    if not log_channel_id:
        await interaction.response.send_message("Log channel not set!")
        return

    log_channel = bot.get_channel(log_channel_id)

    if action == "restart":
        result = rcon.run_command("DoExit")
        embed = create_log_embed("Server Restart", result)
        await log_channel.send(embed=embed)
        await interaction.response.send_message("Server restart logged.")
    elif action == "save":
        result = rcon.run_command("SaveWorld")
        embed = create_log_embed("Server Save", result)
        await log_channel.send(embed=embed)
        await interaction.response.send_message("Server save logged.")
    else:
        await interaction.response.send_message("Invalid action.")
