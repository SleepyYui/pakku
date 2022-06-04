import discord
from discord.ext import commands
from discord.commands import permissions
from datetime import timedelta
from decouple import config
import database.dbcon as db


class main_moderation(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await member.ban(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " banned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.ban(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were banned on {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Banned {member.mention}", delete_after=10)
        except:
            await member.ban(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " banned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.ban(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Banned {member.mention}", delete_after=10)

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id="NoID"):
        try:
            await ctx.message.delete()
        except:
            pass
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
                db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " unbanned " + str(user.id))
            except:
                await ctx.send(f"Can't find {user.name}", delete_after=10)
        except:
            await ctx.send(f"User does not exist", delete_after=10)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await member.kick(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were kicked from {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Kicked {member.mention}", delete_after=10)
        except:
            await member.kick(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Kicked {member.mention}", delete_after=10)

    @commands.command(name="mute")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        duration = timedelta(hours = 24)
        try:
            await member.timeout_for(duration, reason=reason)
            db.Server.Add.action(str(ctx.guild.id),str( ctx.message.author.id) + " muted " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.mute(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were muted on {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Muted {member.name}", delete_after=10)
        except:
            await member.mute(duration, reason=reason)
            db.Server.Add.action(str(ctx.guild.id),str( ctx.message.author.id) + " muted " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.mute(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Muted {member.name}", delete_after=10)

    @commands.command(name="unmute")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def unmute(self, ctx, member : discord.Member):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await member.remove_timeout()
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " unmuted " + str(member.id))
            await ctx.send(f"Unmuted {member.name}", delete_after=10)
        except:
            await ctx.send(f"Can't unmute {member.name}", delete_after=10)

    @commands.command(name="warn")
    async def warn(self, ctx, member : discord.Member, *, reason=None):
        try:
            ctx.message.delete()
        except:
            pass
        try:
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " warned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.warn(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were warned on {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Warned {member.name}", delete_after=10)
        except:
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " warned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.warn(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Warned {member.name}", delete_after=10)

    @commands.command(name="noteuser")
    async def noteuser(self, ctx, member : discord.Member, *, note=None):
        try:
            await ctx.message.delete()
        except:
            pass
        if note is None:
            await ctx.send(f"Please enter a note", delete_after=10)
        else:
            try:
                db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " noted " + str(member.id) + " for " + str(note))
                db.Server.User.Add.note(str(ctx.message.guild.id), str(member.id), str(note))
                await ctx.send(f"Added note to {member.name}", delete_after=10)
            except:
                await ctx.send(f"Can't add note to {member.name}", delete_after=10)


def setup(client):
    client.add_cog(main_moderation(client))
