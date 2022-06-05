import discord
from discord.ext import commands
from datetime import datetime
from decouple import config
import database.dbcon as db
from discord import Embed

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

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        embed = Embed(title="Server Info", color=discord.Color.blue(), timestamp=datetime.now())
        embed.set_thumbnail(url=ctx.guild.icon)
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        #bans = await ctx.guild.bans().flatten()
        fields = [("Owner:", ctx.guild.owner, True),
            ("Region:", ctx.guild.region, True),
            ("Server ID:", ctx.guild.id, True),
            ("Created at:", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
            ("Members:", len(ctx.guild.members), True),
            ("Humans:", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
            ("Bots:", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
            #("Banned members:", len(bans), True),
            ("Members Statuses:", f"🟢 {statuses[0]}\n🟠 {statuses[1]}\n🔴 {statuses[2]}\n⚪ {statuses[3]}", False),
            #("Categories:", len(ctx.guild.categories), True),
            #("Text channels:", len(ctx.guild.text_channels), True),
            #("Voice channels:", len(ctx.guild.voice_channels), True),
            #("Roles:", len(ctx.guild.roles), False),
            ("Valid Invites:", len(await ctx.guild.invites()), True),
            ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.respond(embed=embed)

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, user: discord.Member):
        try:
            await ctx.message.delete()
        except:
            pass
        embed = discord.Embed(title="User Info", color=discord.Color.blue(), timestamp=datetime.now())
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="Username:", value=user.name, inline=True)
        embed.add_field(name="Nickname:", value=user.nick, inline=True)
        embed.add_field(name="ID:", value=user.id, inline=True)
        embed.add_field(name="Status:", value=user.status, inline=True)
        embed.add_field(name="Joined at:", value=user.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
        embed.add_field(name="Created at:", value=user.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
        embed.add_field(name="Roles:", value=", ".join([x.name for x in user.roles]), inline=True)
        embed.add_field(name="Bot:", value=user.bot, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        embed = discord.Embed(title="Pong!", color=discord.Color.blue(), timestamp=datetime.now())
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.add_field(name="Latency:", value=f"{round(self.client.latency * 1000)}ms", inline=True)
        #embed.add_field(name="Uptime:", value=f"{round(time.time() - self.client.uptime)}s", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(main_server(client))