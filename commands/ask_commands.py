import discord
from discord import app_commands
from arkbot import bot
import openai
import os

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@bot.tree.command(name="ask", description="Ask any question to ChatGPT.")
@app_commands.describe(question="Your question to ChatGPT")
async def ask(interaction: discord.Interaction, question: str):
    # Notify the user that their question is being processed
    await interaction.response.defer()

    try:
        # Correct usage of the OpenAI API for version 1.0.0+
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can also use "gpt-3.5-turbo" for faster/flexible responses
            messages=[{"role": "user", "content": question}],
            max_tokens=200  # Adjust this as per your needs
        )

        # Extract the answer from the API response
        answer = response['choices'][0]['message']['content']

        # Create an embed with the question and ChatGPT's response
        embed = discord.Embed(title="ChatGPT Response", description=answer, color=discord.Color.blue())
        embed.add_field(name="Question", value=question, inline=False)
        embed.set_footer(text="Powered by OpenAI's GPT-4")

        # Send the response embed back to the user
        await interaction.followup.send(embed=embed)

    except Exception as e:
        # Handle potential errors with the API call or response
        await interaction.followup.send(f"An error occurred: {str(e)}")
