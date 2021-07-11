import voxelbotutils as vbu


class FunCommands(vbu.Cog):

    def __init__(self, bot):
        super().__init__(bot)

    @vbu.command(name='test')
    async def _test_command(self, ctx:vbu.Context):
        """
        Test command.
        """

        await ctx.send("One on food, right?")

    @vbu.command(name='ily')
    async def _ily_command(self, ctx:vbu.Context):
        """
        Sometimes we just need to hear this
        """

        custom_responses = {
            488130273662337034: 'I LOVE YOU SO MUCH LIZ', # lizxberry#1212
            449966150898417664: 'Sure, ily ig... ~~weirdo~~', # Vanguard#4805
        }
        try:
            await ctx.send(custom_responses[ctx.author.id])
        except KeyError:
            await ctx.send(f'ilyt, my good friend {ctx.author.name}')
    
    @vbu.command(name='suggest')
    async def _suggest_command(self, ctx:vbu.Context, *, suggestion:str):
        """
        Suggest new features!
        """
        with vbu.Embed(use_random_colour=True) as embed:
            embed.set_author_to_user(ctx.author)
            embed.description = suggestion
        channel = await self.bot.get_channel(861992789318565908) # Suggestions channel
        await ctx.send("Thank you for your suggestion")
    
    @vbu.command(name='credits')
    async def _credits_command(self, ctx:vbu.Context):
        """
        Bot credits
        """

        await ctx.send("I would just like to say thank you to Medusa, Schlöpp and Kae for motivating me to make a bot as they put this idea into my head and helped me to learn code :) ~Liz")
    
    @vbu.command(name='about')
    async def _about_command(self, ctx:vbu.Context):
        """
        Tells you about the bot!
        """

        await ctx.send("Beere tells you many things about food! (No, the name isn't beer, it's berry in German)\nYou should run the help command for all commands.\n\nHowever, if you came here to know more- LizBot, as it was orginally known, was created on the 12th of March 2021 out of boredom by an individual called Liz so they could study for their final exam.\n\nHi, I am Liz. I am currently a student who is aspiring to become a nutritionst as I have a passion for food and science, join the server if you wanna come hang!")


def setup(bot:vbu.Bot):
    x = FunCommands(bot)
    bot.add_cog(x)
