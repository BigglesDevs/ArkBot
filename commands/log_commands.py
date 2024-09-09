import discord
from discord import app_commands
from utils.mongo_manager import MongoManager
from arkbot import bot

mongo_manager = MongoManager()

@bot.tree.command(name="setlogchannel", description="Set a log channel for the bot")
async def set_log_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    mongo_manager.set_channel("log", channel.id)
    await interaction.response.send_message(f"Log channel set to {channel.mention}.")

@bot.tree.command(name="setplayeractivitychannel", description="Set a player activity log channel for the bot")
async def set_player_activity_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    mongo_manager.set_channel("player_activity", channel.id)
    await interaction.response.send_message(f"Player activity channel set to {channel.mention}.")

@bot.tree.command(name="settribelogchannel", description="Set a tribe log channel for the bot")
async def set_tribe_log_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    mongo_manager.set_channel("tribe_log", channel.id)
    await interaction.response.send_message(f"Tribe log channel set to {channel.mention}.")
