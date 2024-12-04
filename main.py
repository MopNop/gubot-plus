import discord
from discord.ext import commands
import asyncio
import os
import glob
import sys
import sqlite3
import pyfiglet
from colorama import Fore
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


intents = discord.Intents.all()
mentions = discord.AllowedMentions(everyone=False, users=True, roles=False)
bot = commands.Bot(command_prefix='.', intents=intents, application_id=1253050889774698577)


@bot.event
async def on_ready():
    print(Fore.LIGHTRED_EX + pyfiglet.figlet_format("guhbot", font="slant"))
    print(Fore.LIGHTWHITE_EX + f'logged in as {bot.user.name} - {bot.user.id} ({discord.__version__})')
    print(Fore.RESET)
    bot.startup_time = discord.utils.utcnow()


async def load():
    for file_path in glob.glob('./cogs/**/*.py', recursive=True):
        module_name = os.path.splitext(os.path.relpath(file_path, start='./cogs'))[0].replace(os.sep, '.')
        await bot.load_extension(f'cogs.{module_name}')


async def main():
    await load()
    await bot.start(TOKEN, reconnect=True)


asyncio.run(main())
