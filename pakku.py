
#pip install -r requirements.txt

import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from datetime import datetime
from datetime import date
import json
from discord.ext.commands import CommandNotFound
import os
from discord.utils import get
import schedule
from discord.ext.commands import MemberNotFound
from discord.ext.commands import MissingPermissions
from decouple import config




client = commands.Bot(command_prefix=["pk ", "Pk ", "PK ", "pk", "Pk", "PK"], intents=discord.Intents.all(), case_insensitive=True)
client.remove_command('help')



@client.event
async def on_ready():
    print("Bot is online")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="anime"), status=discord.Status.online)
    client.start_time = datetime.now()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

    if isinstance(error, MemberNotFound):
        await ctx.send("Can't find this member", delete_after=10)
        return

    if isinstance(error, MissingPermissions):
        await ctx.send("I don't have the permissions to do this", delete_after=10)
        return
    raise error


@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(error)
    else:
        raise error


initial_extensions = []
for directory in os.listdir('./cogs'):
    if directory != '__pycache__' and directory != 'testing':
        for filename in os.listdir('./cogs/' + directory):
            #print(filename)
            if filename.endswith(".py"):
                if filename != 'importantfunctions.py':
                    initial_extensions.append("cogs." + directory + '.' + filename[:-3])
                    print(directory + "/" + filename[:-3] + ".py was loaded successfully")


if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(config('TOKEN'))