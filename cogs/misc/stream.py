import logging
import time

import discord
from discord import app_commands
from discord.ext import commands

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(filename)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler(f"logs/{time.strftime('%m-%d-%Y %H %M %S', time.localtime())}.log")

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s | %(message)s', '%m/%d/%Y %H:%M:%S')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)


class stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    stream = app_commands.Group(name="stream", description="Group of commands in relation to streaming.")
    
    @stream.command(name="start", description="TBA")
    @app_commands.checks.has_permissions(administrator=True)
    async def stream_start(interaction: discord.Interaction) -> None:
        return await interaction.response.send_message(content="*This command is not currently finished!*", ephemeral=True)
    
    
    @stream.command(name="end", description="TBA")
    @app_commands.checks.has_permissions(administrator=True)
    async def stream_end(interaction: discord.Interaction) -> None:
        return await interaction.response.send_message(content="*This command is not currently finished!*", ephemeral=True)

def setup(client: commands.Bot):
    client.add_cog(stream(client))
    logger.info(f"cogs.misc.stream.py Successfully Loaded!")