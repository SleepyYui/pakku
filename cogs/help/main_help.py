import discord
from discord.ext import commands
from requests import delete
import cogs.help.importantfunctions as impf

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    def member_is_moderator(self, member):
        if member.guild_permissions.kick_members or member.guild_permissions.ban_members or member.guild_permissions.administrator or member.guild_permissions.manage_messages or member.guild_permissions.manage_guild or member.guild_permissions.moderator:
            return True
        else:
            return False

    @commands.command(name="help")
    async def help(self, ctx, arg=None, subarg=None):
        try:
            await ctx.message.delete()
        except:
            pass
        if arg is None:
            await ctx.send(embed=impf.Help.general(self.client))
            return
        if subarg != None:
            subarg = subarg.lower()
        arg = arg.lower()
        if arg == "general":
            await ctx.send(embed=impf.Help.general(self.client))
            return
        elif arg == "moderation":
            if self.member_is_moderator(ctx.author) == False:
                await ctx.send("You don't have permission to use this command.", delete_after=10)
                return
            if subarg is None:
                await ctx.send(embed=impf.Help.Moderation.all(self.client))
            elif subarg == "modlogs":
                await ctx.send(embed=impf.Help.Moderation.modlogs(self.client))
            elif subarg == "serverlogs":
                await ctx.send(embed=impf.Help.Moderation.serverlogs(self.client))
            elif subarg == "kick":
                await ctx.send(embed=impf.Help.Moderation.kick(self.client))
            elif subarg == "ban" or subarg == "unban":
                await ctx.send(embed=impf.Help.Moderation.ban(self.client))
            elif subarg == "mute" or subarg == "unmute":
                await ctx.send(embed=impf.Help.Moderation.mute(self.client))
            elif subarg == "warn":
                await ctx.send(embed=impf.Help.Moderation.warn(self.client))
            elif subarg == "note" or subarg == "notes" or subarg == "noteuser":
                await ctx.send(embed=impf.Help.Moderation.noteuser(self.client))
            else:
                await ctx.send(embed=impf.Help.Moderation.all(self.client))
        elif arg == "server":
            if subarg is None:
                await ctx.send(embed=impf.Help.Server.all(self.client))
            elif subarg == "info" or subarg == "serverinfo":
                await ctx.send(embed=impf.Help.Server.serverinfo(self.client))
            elif subarg == "purge" and self.member_is_moderator(ctx.author) == True:
                await ctx.send(embed=impf.Help.Server.purge(self.client))
            elif subarg == "serverinfo":
                await ctx.send(embed=impf.Help.Server.serverinfo(self.client))
            else:
                await ctx.send(embed=impf.Help.Server.all(self.client))
        elif arg == "additional":
            if subarg is None:
                await ctx.send(embed=impf.Help.Additional.all(self.client))
            elif subarg == "ping":
                await ctx.send(embed=impf.Help.Additional.ping(self.client))
            elif subarg == "prefix":
                await ctx.send(embed=impf.Help.Additional.prefix(self.client))
            elif subarg == "userinfo":
                await ctx.send(embed=impf.Help.Additional.userinfo(self.client))
            elif subarg == "botinfo":
                await ctx.send(embed=impf.Help.Additional.botinfo(self.client))
            else:
                await ctx.send(embed=impf.Help.Additional.all(self.client))
        else:
            await ctx.send(embed=impf.Help.general(self.client))


def setup(client):
    client.add_cog(help(client))