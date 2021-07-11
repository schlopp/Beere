import random

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

    @vbu.command(name='foodpun', aliases=['quip', 'fp'])
    async def _food_pun_command(self, ctx:vbu.Context):
        """
        Gives you a cute message
        """

        food_puns = [
            "You're a little cheesy but still grate!",
            "I hope you have a rice day!",
            "Remember that nothing is impopsicle! <3",
            "Thank you for being mango-nificent",
            "Lettuce have a great day!",
            "Everything is gonna brie alright",
            "Donut give up",
            "I hope you get lots of hugs and quiches today!",
            "You're looking gouda :)",
            "Spread hap-pea-ness",
            "You're a cu-tea :)",
            "We're the perfect pear!",
            "We are friend-chip goals :D",
            "Remember that life's batter with cake!",
            "Donut worry, be happy :)",
            "You're fudgin' great",
            "I a-durian you <3",
            "I am berry grateful for you",
            "I cereal-sly adore you",
            "You're one tough cookie!",
            "Beet true to yourself",
            "Always be grape-ful!",
            "You're one in a melon!",
            "Sending you some encouragemint!",
            "You are a cute cucumber!",
            "You have a pizza my heart"
        ]
        await ctx.send(random.choice(food_puns))
    
    @vbu.command(name='foodfact', aliases=['ff', 'fact'])
    async def _food_fact_command(self, ctx:vbu.Context):
        """
        Gives you a fun food fact
        """

        food_facts = [
            "Hawaiian pizza wasn't invented in Hawaii but in Canada!",
            "Most wasabi is horseradish dyed green as real wasabi is difficult to grow and very expensive",
            "Cashews grow on apples called cashew apples :)",
            "Lemons float in water but limes sink!",
            "A single spaghetti noodle is called a 'spaghetto' (Liz speaks Italian, she'd know)",
            "Ketchup was once used as a medicine",
            "Fruit is defined by whether or not it has seeds so tomatoes, pumpkin, olives, and chilli are all fruits as they have seeds",
            "Berries are defined by how they grow, meaning bananas are berries but strawberries are not",
            "A chewed mass of food in the mouth is called a bolus",
            "A food mass within the stomach is called a chyme",
            "Carrots were originally purple",
            "People once thought that tomatoes were poisonous as their acidic nature would leach the lead from the lead plates that they were on",
            "Apple seeds are poisonous but one or few seeds doesn't contain enough amygdalin, a cyanogenic glycoside composed of cyanide and sugar, to harm humans",
            "French fries were invented in Belgium, not France",
            "Some individuals have a gene that makes coriander or cilantro taste like soap",
            "Arachibutyrophobia is the fear of peanut butter sticking to the roof of your mouth",
            "Apples float in water, because 25%% of their volume is made of air",
            "Beere means berry in German!",
            "A single gnocchi is called a 'gnocco' (Liz speaks Italian, she'd know)",
        ]
        await ctx.send(random.choice(food_facts))


def setup(bot:vbu.Bot):
    x = FunCommands(bot)
    bot.add_cog(x)
