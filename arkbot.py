import discord
from discord.ext import commands
from utils.logger import setup_logger
from config.config_manager import ConfigManager

logger = setup_logger()
config = ConfigManager()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Import all commands
from commands.admin_commands import *
from commands.log_commands import *
from commands.dino_commands import *
from commands.status_commands import *
from commands.ask_commands import *

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()  # Syncs all slash commands with Discord
    print("Slash commands synced!")

bot.run(config.DISCORD_TOKEN)
