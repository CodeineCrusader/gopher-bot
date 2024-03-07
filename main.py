import logging
import os
import platform
import random
import time

import colorama
import discord
import jishaku
from discord import app_commands, ui
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord.utils import get
from discordrp import Presence
from dotenv import dotenv_values

from embed_generator import embed_generator

config = dotenv_values(".env")

colorama.init(autoreset=True)

dir_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(f'{dir_path}\\logs'):
    os.makedirs(f'{dir_path}\\logs')

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

@tasks.loop(minutes=1)
async def status():
    choices = [
        discord.Activity(type=discord.ActivityType.playing, name="Games"),
    ]
    chosen = random.choice(choices)
    await client.change_presence(activity=chosen)


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(config["BOT_PREFIX"]), case_insensitive=True, intents=discord.Intents.all())
        self.cogs_list = [
            'jishaku',
            'cogs.moderation.ban', 'cogs.moderation.kick', 'cogs.moderation.softban', 'cogs.moderation.timeout', 'cogs.moderation.warn', 
            'cogs.misc.stream', 'cogs.misc.update_role'
        ]
        
    async def is_owner(self, user: discord.User):
        if user.id == 315336291581558804:
            return True
        return await super().is_owner(user)
    
    async def setup_hook(self):
        for ext in self.cogs_list:
            await self.load_extension(ext)

    async def on_ready(self):
        logger.info(f"Logging in as {self.user.name}")
        logger.info(f"Client ID: {self.user.id}")
        logger.info(f"Discord Version: {discord.__version__}")
        logger.info(f"Python Version: {platform.python_version()}")
        status.start()
        logger.info(f"Status Loop Started")

        channel = client.get_channel(1215108788995096686)
        await channel.send(f'{client.user.mention} is now online!')
        
client = Client()
client.remove_command("help")


@client.event
async def on_member_join(member):
    if member.guild.id == 1149212300927053915:
        channel = client.get_channel(1215029341776510996)
        await channel.send(content=f"Welcome {member.mention} to The Gopher Hole! Please be sure to read <#1149240412410740836> and be sure to check out our <#1215028753969975306> for more information for the server!")
        await member.add_roles(get(member.guild.roles, name="Community Member"))


if __name__ == "__main__":
    client.run(token=config["BOT_TOKEN"])