import typing

import voxelbotutils as vbu
import discord
from discord.ext import commands


class ChemistryCommands(vbu.Cog):

    def __init__(self, bot):
        super().__init__(bot)
    
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        """
        Reading DMs
        """
        # Prevent endless loop
        if message.author.id == self.bot.user.id:
            return

        # If the message is not in a guild
        if not message.guild:
            # Define the log channel with guild ID and channel ID
            logchannel = self.bot.get_guild(853993871565389824).get_channel(855364749406765076)

            # Send a message as embed in that log channel
            embed = discord.Embed(title="Chatting", colour=0x000, description=f"**From:** {message.author.mention}\n\n*{message.content}*")
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await logchannel.send(embed=embed)


def setup(bot:vbu.Bot):
    x = ChemistryCommands(bot)
    bot.add_cog(x)
