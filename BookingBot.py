"""Discord Bot for booking event slots

Author: Henry Chen
Last modified: August 12, 2023

This file contains the actual code for running the bot
"""
import discord
from discord.ext import commands

TOKEN = ...   # TO DO generate actual token

# initialise the client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)


def run_discord_bot():
    """Runs the bot"""

    # when the bot gets started, it will call this
    @client.event
    async def on_ready():
        """When the bot gets started, it will call this"""
        activity = discord.Game(name='Looking for bookings', type=1)
        await client.change_presence(status=discord.Status.online, activity=activity)
        print(f'{client.user} is now running!')

        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)

    @client.hybrid_command(description='Check for bookings')
    async def check_bookings(ctx):
        """Searches for bookings"""
        ...   # TO DO: Create a web crawler to check the bookings, then return the result

    client.run(TOKEN)
