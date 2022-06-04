import discord
from discord.ext import commands
from discord.commands import permissions

class moderation_help(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(moderation_help(client))