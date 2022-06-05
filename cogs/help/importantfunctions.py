
import discord
from regex import R
from datetime import datetime

class Help:
    def __init__(self, client):
        self.client = client

    def general(self):
        embed = discord.Embed(title="Help", description="This is the help command.", color=discord.Color.blue())#, timestamp=datetime.now())
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/741938289547804713/d0b9900170ec1b95fc01e222c94f3944.png")
        embed.add_field(name="`pk help`", value="Shows this message.", inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        #embed.add_field(name="`pk help <command>`", value="Shows help for a command.", inline=False)
        #embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="`pk help <category>`", value="Shows help for a category.\nThose are: ```\nModeration\nServer\nAdditional``` as of now.", inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="`pk help <category> <command>`", value="Shows help for a command in a category.", inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="`pk help <category> <command> <subcommand>`", value="Shows help for a subcommand in a command in a category. -> The same as `pk help <command> <subcommand>`\n*This command is not working as of now.*", inline=False)
        return embed

    class Moderation:
        def __init__(self, client):
            self.client = client

        def all(self):
            embed=discord.Embed(title="Moderation Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="Banning", value="You can ban members from your Server by using this command. It works with the Name, ID and if you ping the user. `pk ban @user` or `pk ban 1234656789`\nYou can unban users by typing in their ID.\n`pk unban 123456789`", inline=False)
            embed.add_field(name="Kicking", value="You can kick members from your Server by using this command. It works with the Name, ID and if you ping the user. `pk kick @user` or `pk kick 1234656789`", inline=False)
            embed.add_field(name="Muting", value="You can mute members on your Server by using this command. It works with the Name, ID and if you ping the user. `pk mute @user 1d Insults` or `pk mute 1234656789` -> Not specifying a Timespan will mute them for 24 hours. You can unmute users by typing in their ID, Name or mentioning them, just like when muting. `pk unmute 123456789`", inline=False)
            embed.add_field(name="Warning", value="You can warn users on your Server, to let them know that they did something wrong.It works with the Name, ID and if you ping the user. `pk warn @user Insults` or `pk warn 123456789 Insults` Remember that this will send a message to the user. If you don't want a message to be sent for whatever reason, please use `noteuser`", inline=False)
            embed.add_field(name="Noting", value="You can note down a member of your Server to let your other moderators know what they did. It works with the Name, ID and if you ping the user. `pk noteuser @user The User Insulted other Users` or `pk noteuser 123456789 The User Insulted other Users`", inline=False)
            embed.add_field(name="Modlogs", value="You can view the Modlogs of a Member, this includes Notes, Warns, Bans, Kicks and Mutes. It works with the Name, ID and if you ping the user. `pk modlogs @user`", inline=False)
            embed.add_field(name="Serverlogs", value="You can view the Serverlogs of this server, this includes the last few moderative actions taken on your server. `pk serverlogs`", inline=False)
            return embed

        def modlogs(self):
            embed=discord.Embed(title="Modlogs Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk modlogs @user`", value="Views the Modlogs of a Member, this includes Notes, Warns, Bans, Kicks and Mutes. It works with the Name, ID and if you ping the user. `pk modlogs @user`", inline=False)
            embed.add_field(name="Permissions", value="You need the `view_audit_log` permission to use this command.", inline=False)
            return embed

        def serverlogs(self):
            embed=discord.Embed(title="Serverlogs Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk serverlogs`", value="Views the Serverlogs of this server. `pk serverlogs`", inline=False)
            embed.add_field(name="Permissions", value="You need the `moderate_members` permission to use this command.", inline=False)
            return embed

        def ban(self):
            embed=discord.Embed(title="Ban Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk ban @user`", value="Bans a user from your Server. It works with the Name, ID and if you ping the user. `pk ban @user` or `pk ban 1234656789`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="`pk unban 123456789`", value="Unbans a user from your Server. It ONLY works with the ID. `pk unban 123456789`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `ban_members` permission to use this command.", inline=False)
            return embed

        def kick(self):
            embed=discord.Embed(title="Kick Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk kick @user`", value="Kicks a user from your Server. It works with the Name, ID and if you ping the user. `pk kick @user` or `pk kick 1234656789`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `kick_members` permission to use this command.", inline=False)
            return embed

        def mute(self):
            embed=discord.Embed(title="Mute Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk mute @user`", value="Mutes a user for 1 day. You can also specify a Timespan. `pk mute @user 1d Insults` or `pk mute 1234656789 1d Insults` -> Not specifying a Timespan will mute them for 24 hours.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="`pk unmute @user`", value="Unmutes users by typing in their ID, Name or mentioning them, just like when muting. `pk unmute 123456789`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `moderate_members` permission to use this command.", inline=False)
            return embed

        def warn(self):
            embed = discord.Embed(title="Warn Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk warn @user`", value="Warns a user. It works with the Name, ID and if you ping the user. `pk warn @user Insults` or `pk warn 123456789 Insults` Remember that this will send a message to the user. If you don't want a message to be sent for whatever reason, please use `noteuser`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `moderate_members` permission to use this command.", inline=False)
            return embed

        def noteuser(self):
            embed = discord.Embed(title="Note Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://assets-global.website-files.com/5f9072399b2640f14d6a2bf4/615e08a57562b757afbe7032_TransparencyReport_BlogHeader.png")
            embed.add_field(name="`pk noteuser @user`", value="Notes a user. It works with the Name, ID and if you ping the user. `pk noteuser @user The User Insulted other Users` or `pk noteuser 123456789 The User Insulted other Users`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `moderate_members` permission to use this command.", inline=False)
            return embed

    class Server:
        def __init__(self, client):
            self.client = client

        def all(self):
            embed=discord.Embed(title="Server Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://www.trendingus.com/wp-content/uploads/2021/09/Trending-Discord-Bots-to-Game-Up-Your-Server-scaled.jpg")
            embed.add_field(name="`pk serverinfo`", value="Shows information about your Server.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="`pk purge`", value="Deletes a specified amount messages in the current channel. `pk purge <amount>`", inline=False)
            return embed

        def serverinfo(self):
            embed=discord.Embed(title="Serverinfo Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://www.trendingus.com/wp-content/uploads/2021/09/Trending-Discord-Bots-to-Game-Up-Your-Server-scaled.jpg")
            embed.add_field(name="`pk serverinfo`", value="Shows information about your Server.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `manage_messages` permission to use this command.", inline=False)
            return embed

        def purge(self):
            embed=discord.Embed(title="Purge Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://www.trendingus.com/wp-content/uploads/2021/09/Trending-Discord-Bots-to-Game-Up-Your-Server-scaled.jpg")
            embed.add_field(name="`pk purge`", value="Deletes a specified amount messages in the current channel. `pk purge <amount>`", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Permissions", value="You need the `manage_messages` permission to use this command.", inline=False)
            return embed

    class Additional:
        def __init__(self, client):
            self.client = client

        def all(self):
            embed=discord.Embed(title="Additional Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/908828/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png")
            embed.add_field(name="`pk ping`", value="Shows the latency of the bot.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="`pk userinfo`", value="Shows information about a user.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="`pk serverinfo`", value="Shows information about your Server.", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Prefix", value="The prefixes are `pk`, `pk `, `Pk `, `PK `, `Pk` and `PK`", inline=False)
            return embed

        def ping(self):
            embed=discord.Embed(title="Ping Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/908828/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png")
            embed.add_field(name="`pk ping`", value="Shows the latency of the bot.", inline=False)
            return embed

        def prefix(self):
            embed=discord.Embed(title="Prefix Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/908828/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png")
            embed.add_field(name="Prefix", value="The prefixes are `pk`, `pk `, `Pk `, `PK `, `Pk` and `PK`", inline=False)
            return embed

        def userinfo(self):
            embed=discord.Embed(title="Userinfo Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/908828/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png")
            embed.add_field(name="`pk userinfo @user`", value="Shows information about a user.", inline=False)
            return embed

        def botinfo(self):
            embed=discord.Embed(title="Botinfo Help", color=discord.Color.blue())#, timestamp=datetime.now())
            embed.set_thumbnail(url="https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/908828/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png")
            embed.add_field(name="`pk botinfo`", value="Shows useful information about the bot.", inline=False)
            return embed

