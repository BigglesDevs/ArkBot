import discord
from discord import app_commands
from utils.embeds import create_log_embed
from utils.mongo_manager import MongoManager
from arkbot import bot

# Initialize MongoDB manager
mongo_manager = MongoManager()

@bot.tree.command(name="track-dino", description="Track a dino's health and food")
@app_commands.describe(dino_name="Name of the dino", health="Dino's health", food="Dino's food")
async def track_dino(interaction: discord.Interaction, dino_name: str, health: int, food: int):
    # Insert dino stats into MongoDB
    mongo_manager.db['dino_stats'].insert_one({
        "dino_name": dino_name,
        "health": health,
        "food": food
    })

    # Create a log embed with dino stats
    embed = create_log_embed("Dino Tracked", f"Tracking {dino_name} with health {health} and food {food}.")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="dino-list", description="List all tracked dinos")
async def dino_list(interaction: discord.Interaction):
    # Fetch all tracked dinos from MongoDB
    dinos = mongo_manager.db['dino_stats'].find()

    dino_list_str = "\n".join([f"{dino['dino_name']} - Health: {dino['health']}, Food: {dino['food']}" for dino in dinos])
    
    if dino_list_str:
        embed = create_log_embed("Tracked Dinos", dino_list_str)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("No dinos currently tracked.")

@bot.tree.command(name="remove-dino", description="Remove a dino from tracking")
@app_commands.describe(dino_name="Name of the dino to remove")
async def remove_dino(interaction: discord.Interaction, dino_name: str):
    # Remove the dino from MongoDB
    mongo_manager.db['dino_stats'].delete_one({"dino_name": dino_name})
    
    # Respond with confirmation
    await interaction.response.send_message(f"Dino {dino_name} has been removed from tracking.")
