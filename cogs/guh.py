import discord
from discord import app_commands
from discord.ext import commands
import os
import subprocess
import random

cog_name = os.path.basename(__file__)[:-3]

guh = ["images/guh1.jpg",
       "images/guh2.jpg",
       "images/guh3.jpg",
       "images/guh4.jpg",
       "images/guh5.jpg",
       "images/guh6.jpg"]


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} cog loaded')

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if 'guh' in ctx.content.lower():
            await ctx.reply(file=discord.File(random.choice(guh)))


async def setup(bot):
    await bot.add_cog(Ping(bot), guilds=[discord.Object(id=1252713098507452506)])
