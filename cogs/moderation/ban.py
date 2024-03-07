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


class ban(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="ban", description="TBA")
    @app_commands.checks.has_permissions(administrator=True)
    async def stream_start(self, interaction: discord.Interaction, user: discord.Member) -> None:
        await interaction.response.send_message(content="*This command is not currently finished!*", ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(ban(client))
    logger.info(f"cogs.moderation.ban.py Successfully Loaded!")