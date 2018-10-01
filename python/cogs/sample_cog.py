"""This is a cog for a discord.py bot.
SAMPLE

Load the cog by calling client.load_extension with the name of this python file
as an argument (without .py)
    example:    bot.load_extension('example')
or by calling it with the path and the name of this python file
    example:    bot.load_extension('folder.example')

"""

from discord.ext import commands
from discord import Member


class COG_CLASS_NAME():
    def __init__(self, client):
        self.client = client


    async def __local_check(self, ctx):
        """This check will automatically be applied to each command contained
        in this cog.
        Use it to decide who can use the commands in this cog.
        If this returns False, the user calling the command (ctx.message.author)
        can not use the command and will not see the command in the bot help.
        In the current state, the check will only return True if the bot owner
        executed a command
        """
        if await ctx.bot.is_owner(ctx.author):
            return True
        # Put checks here

    # ----------------------------------------------
    # Cog Event listeners
    # ----------------------------------------------
    async def on_message(self, msg):
        """This event is called every time the bot sees a new message.
        This event does not replace the bot's normal on_message event.
        It runs and in parallel to the nomal on_message event and
        all other on_message events contained in other cogs.
        """
        print(msg.content)
        # put stuff here

    # Some useful events are
    # on_connect()
    # on_ready()
    # on_typing(channel, user, when)
    # on_message(message)
    # on_message_delete(message)
    # on_message_edit(msg_before, msg_after)
    # on_reaction_add(reaction, user)
    # on_reaction_remove(reaction, user)
    # on_reaction_clear(message, reactions)
    # https://discordpy.readthedocs.io/en/rewrite/api.html#event-reference

    # ----------------------------------------------
    # Cog Commands
    # ----------------------------------------------
    @commands.command(
        name='example', # if this is omitted the function name will be used
        brief='brief description', # shown when users execute "help"
        description='description', # shown when users execute "help example"
        aliases=['name2', 'name3'], # alternative ways to execute the command
        hidden=False, # Hide the command in the bot help
    )
    # More checks possible here - examples:
    # @commands.guild_only() Command cannot be used in private messages.
    # @commands.is_owner() Command can only be used by the bot owner.
    # @commands.is_nsfw() Command can only be used in NSFW channels
    async def COMMAND_NAME(self, ctx, member: Member):
        await ctx.send(f'Hey {member.mention}, how are you?')


def setup(client):
    client.add_cog(COG_CLASS_NAME(client))
