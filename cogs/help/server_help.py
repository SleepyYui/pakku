import discord
from discord.ext import commands
from discord.commands import permissions

class server_help(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(server_help(client))