import discord

def create_log_embed(title, description, color=discord.Color.green()):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="ARK Survival Evolved Bot")
    return embed
