import discord
from discord.ext import commands
from discord.commands import permissions
import json


class standard_moderation(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason) 
            await member.send(f"You were banned on {ctx.message.guild.name}")
            await ctx.send(f"Banned {member.mention}", delete_after=10)
        except:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.mention}", delete_after=10)

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id="NoID"):
        try:
            id = int(id)
        except:
            await ctx.send(f"Please use the ID of the user", delete_after=10)
            return
        try:
            user = await self.client.fetch_user(id)
            try:
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}", delete_after=10)
            except:
                await ctx.send(f"Can't find {user.name}", delete_after=10)
        except:
            await ctx.send(f"User does not exist", delete_after=10)



def setup(client):
    client.add_cog(standard_moderation(client))
