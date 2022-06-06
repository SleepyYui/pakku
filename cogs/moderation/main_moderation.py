from re import A
import discord
from discord.ext import commands
from datetime import datetime, timedelta
from decouple import config
from regex import R
import database.dbcon as db
import humanfriendly


class main_moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    def member_is_moderator(self, member):
        if member.guild_permissions.kick_members or member.guild_permissions.ban_members or member.guild_permissions.administrator:
            return True
        else:
            return False

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        if  self.member_is_moderator(member):
            await ctx.send("You can't ban this member", delete_after=10)
            return False
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
        if self.member_is_moderator(member):
            await ctx.send("You can't kick this member", delete_after=10)
            return False
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
    async def mute(self, ctx, member : discord.Member, timespan, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            timespan = humanfriendly.parse_timespan(timespan)
            duration = timedelta(seconds=timespan)
        except:
            await ctx.send(f"Please use a valid timespan.\n**Example:** `mute 123456789 5h test`\nFor further information, please use `help moderation mute`", delete_after=10)
            return False
            #duration = timedelta(hours = 24)
        if self.member_is_moderator(member):
            await ctx.send("You can't mute this member", delete_after=10)
            return False
        try:
            await member.timeout_for(duration, reason=reason)
            await ctx.send(f"Muted {member.name} for {timespan}s", delete_after=10)
            db.Server.Add.action(str(ctx.guild.id),str( ctx.message.author.id) + " muted " + str(member.id) + " for " + str(timespan) + " for " + str(reason))
            db.Server.User.Add.mute(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were muted on {ctx.message.guild.name} for {reason}")
        except:
            await member.timeout_for(duration, reason=reason)
            await ctx.send(f"Muted {member.name} for {timespan}", delete_after=10)
            db.Server.Add.action(str(ctx.guild.id),str( ctx.message.author.id) + " muted " + str(member.id) + " for " + str(timespan) + " for " + str(reason))
            db.Server.User.Add.mute(str(ctx.message.guild.id), str(member.id), str(reason))

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
            await ctx.send(f"Unmuted {member.name}", delete_after=10)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " unmuted " + str(member.id))
        except:
            await ctx.send(f"Can't unmute {member.name}", delete_after=10)

    @commands.command(name="warn")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def warn(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        if reason == None:
            await ctx.send(f"Please provide a reason", delete_after=10)
            return False
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
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
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

    @commands.command(name="modlogs")
    @commands.has_permissions(view_audit_log=True)
    @commands.bot_has_permissions(view_audit_log=True)
    async def modlogs(self, ctx, member : discord.Member):
        try:
            await ctx.message.delete()
        except:
            pass
        ulogs = db.Server.User.Get.all(str(ctx.guild.id), str(member.id))
        embed = discord.Embed(title=f"{member.name}'s Modlogs", color=member.color)#, timestamp=datetime.now())
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        embed.add_field(name="ID, Nickname, Ping", value=f"ID: {member.id} \nNickname: {member.display_name} \nPing: {member.mention}", inline = False)

        #try:
        if True:
            if ulogs["warns"] != None:
                warns = ""
                for warn in ulogs["warns"]:
                    warns += f"`{warn}`\n"
                embed.add_field(name=f"Warns ({len(ulogs['warns'])})", value=warns, inline = True)
        #except:
        #    pass
        try:
            if ulogs["mutes"] != None:
                mutes = ""
                for mute in ulogs["mutes"]:
                    mutes += f"`{mute}`\n"
                embed.add_field(name=f"Mutes ({len(ulogs['mutes'])})", value=mutes, inline = True)
        except:
            pass
        try:
            if ulogs["kicks"] != None:
                kicks = ""
                for kick in ulogs["kicks"]:
                    kicks += f"`{kick}`\n"
                embed.add_field(name=f"Kicks ({len(ulogs['kicks'])})", value=kicks, inline = True)
        except:
            pass
        try:
            if ulogs["notes"] != None:
                notes = ""
                for note in ulogs["notes"]:
                    notes += f"`{note}`\n"
                embed.add_field(name=f"Notes ({len(ulogs['notes'])})", value=notes, inline = True)
        except:
            pass
        try:
            if ulogs["bans"] != None:
                bans = ""
                for ban in ulogs["bans"]:
                    bans += f"`{ban}`\n"
                embed.add_field(name=f"Bans ({len(ulogs['bans'])})", value=mutes, inline = True)
        except:
            pass
        try:
            if ulogs["proles"] != None:
                proles = ""
                for prole in ulogs["proles"]:
                    proles += f"`{prole}`\n"
                embed.add_field(name=f"Persistant Roles ({len(ulogs['proles'])})", value=mutes, inline = True)
        except:
            pass
        await ctx.send(embed=embed)

    @commands.command(name="serverlogs")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def serverlogs(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        actions = db.Server.Get.actions(str(ctx.guild.id))
        try:
            if actions != None and actions != [] and actions != "None":
                if len('\n'.join(actions[25:])) > 1000:
                    if len('\n'.join(actions[20:])) > 1000:
                        if len('\n'.join(actions[15:])) > 1000:
                            if len('\n'.join(actions[10:])) > 1000:
                                if len('\n'.join(actions[1:])) > 1000:
                                    await ctx.send(f"Too many actions to display", delete_after=10)
                                    return
                                else:
                                    await ctx.send("```" + actions[:1] + "```")
                                    return
                            else:
                                await ctx.send("```" + '\n'.join(actions[:10]) + "```")
                                return
                        else:
                            await ctx.send("```" + '\n'.join(actions[:15]) + "```")
                            return
                    else:
                        await ctx.send("```" + '\n'.join(actions[:20]) + "```")
                        return
                else:
                    await ctx.send("```" + '\n'.join(actions[:25]) + "```")
                    return
            else:
                await ctx.send("There are no actions to display", delete_after=10)
        except:
            await ctx.send("Something went wrong fetching the data...", delete_after=10)

def setup(client):
    client.add_cog(main_moderation(client))
