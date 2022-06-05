import discord
from discord.ext import commands
from datetime import datetime
from decouple import config
import database.dbcon as db
from discord import Embed

class main_bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    #get currently active shards
    def get_active_shards(self):
        return self.client.shard_count

    @commands.command(name="ping")
    async def ping(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        embed = discord.Embed(title="Pong!", color=discord.Color.blue())#, timestamp=datetime.now())
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.add_field(name="Latency:", value=f"{round(self.client.latency * 1000 / int(config('SHARD_COUNT')))}ms", inline=False)
        #embed.add_field(name="Uptime:", value=f"{round(time.time() - self.client.uptime)}s", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        embed = discord.Embed(title="Bot Info", color=discord.Color.blue())#, timestamp=datetime.now())
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))
        shard_id = ctx.guild.shard_id
        shard = self.client.get_shard(shard_id)
        shard_ping = shard.latency
        shard_servers = len([guild for guild in self.client.guilds if guild.shard_id == shard_id])
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.add_field(name='Total Guilds:', value=serverCount, inline=False)
        embed.add_field(name='Total Users:', value=memberCount, inline=False)
        embed.add_field(name='Current Shard-ID:', value=shard_id, inline=False)
        embed.add_field(name='Shard Servers:', value=shard_servers, inline=False)
        embed.add_field(name='Shard Ping:', value=f"{round(shard_ping)}ms", inline=False)
        embed.add_field(name="All Shard Ping:", value=f"{round(self.client.latency * 1000)}ms", inline=False)
        embed.add_field(name="Bot Ping:", value=f"{round(self.client.latency * 1000 / pow(int(config('SHARD_COUNT')), 3))}ms", inline=False)
        #embed.add_field(name="\u200b", value="\u200b", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(main_bot(client))