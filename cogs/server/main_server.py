import discord
from discord.ext import commands
from discord.commands import permissions
from datetime import timedelta
from decouple import config
import database.dbcon as db

class main_server(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await ctx.channel.purge(limit=amount)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " purged " + str(amount) + " messages in " + str(ctx.message.channel.id))
            await ctx.send(f"Deleted {amount} messages.", delete_after=10)
        except:
            #print(str(ctx.guild.id) + "\n" + str(ctx.message.author.id) + " purged " + str(amount) + " messages in " + str(ctx.message.channel.id))
            await ctx.send(f"Can't delete {amount} messages.", delete_after=10)

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send("Command is currently disabled. Please use `purge` instead.", delete_after=10)
        """
        try:
            mgs = []
            async for x in ctx.client.logs_from(ctx.message.channel):
                mgs.append(x)
            await ctx.client.delete_messages(mgs)
            db.Server.Add.action(ctx.guild.id, ctx.message.author.id + " cleared " + ctx.message.channel.id)
        except:
            await ctx.send(f"Can't clear channel", delete_after=10)
        """

def setup(client):
    client.add_cog(main_server(client))