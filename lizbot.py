# Imports the necessary libraries for Discord
from copy import copy
import discord
from discord.ext import commands
import json
import random

# Create the bot variable
bot = commands.Bot(command_prefix=["!liz ", "!Liz ","!b ", "!B "], owner_id=488130273662337034)

@bot.event 
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}') 
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("I am hungry"))
    
# Commands
@bot.command()
async def test(ctx):
    text= "One on food, right?"
    await ctx.send(text)

@bot.command()
async def invite(ctx):
    text="Sorry, this bot isn't public yet but thank you for your support"
    await ctx.send(text)

#generalhelp
bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed()
    embed = discord.Embed(
        colour=discord.Colour(
            random.choice([
                0xB6D7A8, 0x93C47D,
                0xEA9999, 0xE06666,
                ])
            )
        )
    embed.description = "'Food. Food? Food!'"
    embed.title = "General help"
    embed.add_field(
        name="!b help", value="Shows you this command",
        inline = False)
    embed.add_field(
        name="!b server", value="Gives you the server link",
        inline=False)
    embed.add_field(
        name = "!b about", value = "Tells you about the bot!",
        inline = False)
    embed.add_field(
        name = "!b helpfun", value = "Cute commands",
        inline = False)
    embed.add_field(
        name="!b helpcook", value= "Cooking commands!",
        inline=False)
    return await ctx.send(embed = embed)
#funhelp
@bot.command()
async def helpfun(ctx):
    embed = discord.Embed()
    embed = discord.Embed(
        colour=discord.Colour(
            random.choice([
                0xB6D7A8, 0x93C47D,
                0xEA9999, 0xE06666,
                ])
            )
        )
    embed.description = "'Food. Food? Food!'"
    embed.title = "Help for the fun commands"
    embed.add_field(
        name="!b helpfun", value="Shows you this command",
        inline = False)
    embed.add_field(
        name="!b fact", value="Gives you a fun food fact",
        inline=False)
    embed.add_field(
        name="!b quip", value="Gives you a cute message",
        inline=False)
    embed.add_field(
        name = "!b ily", value= "Sometimes we just need to hear this",
        inline=False)
    return await ctx.send(embed=embed)
#helpsci
@bot.command()
async def helpcook(ctx):
    embed = discord.Embed()
    embed = discord.Embed(
        colour=discord.Colour(
            random.choice([
                0xB6D7A8, 0x93C47D,
                0xEA9999, 0xE06666,
                ])
            )
        )
    embed.description = "'Food. Food? Food!'"
    embed.title = "Let's get cooking!"
    embed.add_field(
        name="!b helpcook",
        value="Shows you this command!",
        inline=False)
    embed.add_field(
        name = "!b chem",
        value = "chemical reactions that occur within cooking",
        inline = False)
    embed.add_field(
        name="coming soon",
        value="-",
        inline=False)
    return await ctx.send(embed=embed)

@bot.command()
async def chem(ctx):
    embed = discord.Embed()
    embed = discord.Embed(
        colour=discord.Colour(
            random.choice([
                0xB6D7A8, 0x93C47D,
                0xEA9999, 0xE06666,
                ])
            )
        )
    embed.description = "'Food. Food? Food!'"
    embed.title = "Food chemistry and its reactions!"
    embed.add_field(
        name="!b aeration", 
        value="Tells you about aeration",
        inline=False)
    embed.add_field(
        name="!b caramelisation", 
        value="Tells you about caramelisation",
        inline=False)
    embed.add_field(
        name="!b coagulation",
        value="Tells you about coagulation",
        inline=False)
    embed.add_field(
        name="!b denaturation", 
        value="Tells you about denaturation",
        inline=False)
    embed.add_field(
        name="!b dextrinization", 
        value="Tells you about dextrintization",
        inline=False)
    embed.add_field(
        name="!b emulsification", 
        value="Tells you about emulsification",
        inline=False)
    embed.add_field(
        name="!b gelatinization", 
        value="Tells you about gelatinization",
        inline=False)
    embed.add_field(
        name="!b maillard", 
        value="Tells you about the Maillard reaction",
        inline=False) 
    return await ctx.send(embed=embed)

@bot.command()
async def aeration(ctx):
   text = "Aeration is the process of incorporating air into food products to increase the volume and create a light, airy texture.\nFood can be aerated by:\n-*Biological ingredients:* yeast\n-*Chemical ingredients:* baking powder, bicarbonate of soda.\n-*Mechanical actions:* like sifting, creaming, whisking, beating, folding ingredients and rubbing in ingredients"
   await ctx.send(text)
@bot.command()
async def caramelisation(ctx):
   text = "Caramelisation is when sugar (sucrose) begins to decompose when exposed to high temperatures (190°C or 374°F) using dry heat. An example would be caramel!"
   await ctx.send(text)
@bot.command()
async def coagulation(ctx):
   text = "Coagulation is a form of denaturation (see `!b denaturation` for more info) that occurs when there is a permanent change in the protein from a liquid into a thick mass as a result of heat or the addition of acids. A food example would be cooking eggs"
   await ctx.send(text)
@bot.command()
async def denaturation(ctx):
   text = "Denaturation describes the permanent structural change of the protein molecules in food like beef. This can occur by the application of heat, mechanical action or the addition of acids."
   await ctx.send(text)
@bot.command()
async def dextrinization(ctx):
   text = "Dextrinization is the process that occurs when a starch is exposed to dry heat; the starch is broken down into dextrin which results in a golden brown colour. Found in foods like toast!"
   await ctx.send(text)
@bot.command()
async def emulsification(ctx):
   text = "Emulsification is mixing two immiscible liquids (liquids that don’t normally combine), for example water and oil. Some proteins, like lecithin found in egg yolk, act as emulsifying agents and hold the immiscible liquids in suspension. It is found in foods like mayonnaise."
   await ctx.send(text)
@bot.command()
async def gelatinization(ctx):
   text = "Gelatinization is the process in which starch granules absorb liquid in the presence of heat which causes starch granules to burst and release molecules thus thickening the liquid, forming a gel."
   await ctx.send(text)
@bot.command()
async def maillard(ctx):
   text = "Maillard turns food brown and creates pleasant, volatile, aromatic compounds as seen in foods like cookies It is a reaction between amino acids in protein and sugars or starch and it beings at 154°C (309°F)."
   await ctx.send(text)

@bot.command()
async def git(ctx):
    text= "*git* me a sandwich :)"
    await ctx.send(text)

@bot.command()
async def ily(ctx):
    if ctx.author.id == 488130273662337034:
        text = "I LOVE YOU SO MUCH LIZ"
    if ctx.author.id == 449966150898417664:
        text = "Sure, ily ig... ~~weirdo~~"
    else: text = (f"ilyt, my good friend {ctx.author.name}")
    await ctx.send(text)

@bot.command()
async def suggest(ctx, *, suggestion):
  await bot.get_channel(861992789318565908).send(f"{ctx.author.name} ({ctx.author.id}): {suggestion}")
  await ctx.send("Thank you for your suggestion")

@bot.command() 
async def credits(ctx:commands.Context): 
    text = "I would just like to say thank you to Medusa, Schlöpp and Kae for motivating me to make a bot as they put this idea into my head and helped me to learn code :) ~Liz"
    await ctx.send(text) 

@bot.command() 
async def about(ctx:commands.Context): 
    text = "Beere tells you many things about food! (No, the name isn't beer, it's berry in German)\nYou should run the help command for all commands.\n\nHowever, if you came here to know more- LizBot, as it was orginally known, was created on the 12th of March 2021 out of boredom by an individual called Liz so they could study for their final exam.\n\nHi, I am Liz. I am currently a student who is aspiring to become a nutritionst as I have a passion for food and science, join the server if you wanna come hang!"
    await ctx.send(text) 

@bot.command()
async def server(ctx):
   text = "You can find me in my friend, Ghigeon's, server; https://discord.gg/jagHqTXqeg"
   await ctx.send(text)

@bot.command() 
async def DM(ctx, user: discord.User, *, message=None): 
    message = message or "This message is sent via DM" 
    await user.send(message)

@bot.event
# on_message takes a message argument
async def on_message(message):
    # Prevent endless loop
    if message.author.id == bot.user.id:
        return

    # If the message is not in a guild
    if not message.guild:
        # Define the log channel with guild ID and channel ID
        logchannel = bot.get_guild(853993871565389824).get_channel(855364749406765076)

        # Send a message as embed in that log channel
        embed = discord.Embed(title="Chatting", colour=0x000, description=f"**From:** {message.author.mention}\n\n*{message.content}*")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await logchannel.send(embed=embed)
    await bot.process_commands(message)
        
@bot.command()
# We are defining member as a discord.Member object, it will convert automatically for us
async def dm(ctx, user: discord.User, *, message: str):
    try:
        # Send the message by calling the .send method on the member object
        await user.send(f"{message}")
        await ctx.send(f"Successfully sent message to {user}.")

    # If user is not in guild or has blocked the bot
    except discord.Forbidden:
        await ctx.send(f"Failed to send message to {user}.")

@bot.command(aliases=['foodfact'])
async def fact(ctx):
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
        "Apples float in water, because 25% of their volume is made of air",
        "Beere means berry in German!",
        "A single gnocchi is called a 'gnocco' (Liz speaks Italian, she'd know)",
    ]

    await ctx.send(random.choice(food_facts))

@bot.command(aliases=['foodpun'])
async def quip(ctx):
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

@bot.command()
async def helprec(ctx):
    embed = discord.Embed()
    embed = discord.Embed(
        colour=discord.Colour(
            random.choice([
                0xB6D7A8, 0x93C47D,
                0xEA9999, 0xE06666,
                ])
            )
        )
    embed.description = "'Food. Food? Food!'"
    embed.title = "Cooking time!"
    embed.add_field(
        name="!b recipe [keyword]",
        value= "This will show you a recipe. Without a keyword, you will get a random recipe!",
        inline=False)
    embed.add_field(
        name= "About keywords",
        value= "Keywords incluce ingredients but also words such as sweet, savoury, breakfast, fruit etc.\nThere are also levels from 1 to 5 inclusive, going more complex as you go up in levels.\nIf you want a 'Liz-tested-and-approved' recipe, use the keyword 'liz'.\nAll keywords are lowercase with no spaces",
        inline=False)
    embed.add_field(
        name= "Recipe modifications",
        value="If you have dietary requirements such as allergies, then ask Liz for modifications (Find the Liz by running `!b server`)"
    )
    return await ctx.send(embed=embed)

@bot.command()
async def randomrecipe(ctx, *, tags: str = None):
    with open('lizrec.json') as a:
        data = json.load(a)
    if tags:
        valid_recipes = []
        for r in data:
            if tags.lower() in r['Tags']:
                valid_recipes.append(r)
    else:
        valid_recipes = data
    if not valid_recipes:
        return await ctx.send(f"No recipe related to **{tags}** could be found.\nSee how keywords are used within `!b helprec` or send Liz the recipe you'd like to see (join the server to find me with `!b server`!")
    selected_recipe = random.choice(valid_recipes)
    output = f"This is a recipe for\n**{selected_recipe['name']}**\n*{selected_recipe['Info']}*\n{selected_recipe['Ingredients']}\n{selected_recipe['Method']}"
    await ctx.send(output) 


@bot.command(aliases = ["dietaryrequirement", "dietaryrequirements"])
async def dr(ctx, *, tags: str = None):
    with open('dietaryrequirements.json') as a:
        data = json.load(a)
    if tags:
        valid_dietaryrequirments = []
        for r in data:
            if tags.lower() in r['Tags']:
                valid_dietaryrequirments.append(r)
    else:
        return await ctx.send(f"Please enter a dietary requirement i.e vegan, nuts, lactose, halal etc.")
    if not valid_dietaryrequirments:
        return await ctx.send(f"No dietary requirement related to **{tags}** could be found.")
    selected_dietaryrequirement = random.choice(valid_dietaryrequirments)
    output = f"These are replaces for\n**{selected_dietaryrequirement['name']}**\n*{selected_dietaryrequirement['Info']}*\n{selected_dietaryrequirement['Replacement']}"
    await ctx.send(output) 

#send message as bot
@bot.command() 
async def echo(ctx, *, content:str): 
    if ctx.author.id == 488130273662337034: 
        await ctx.send(content)

@bot.command( hidden = True ) 
@commands.is_owner() 
async def sudo(ctx, victim: discord.Member, *, command):
    """Take control."""
    new_message = copy(ctx.message)
    new_message.author = victim 
    new_message.content = ctx.prefix + command 
    await bot.process_commands(new_message)

@bot.command()
async def say(ctx, channel_id:int, *, text:str):
    if ctx.author.id == 488130273662337034: 
        channel = bot.get_channel(channel_id)
    await channel.send(text)

# Run the bot
with open('config.json') as a:
    data = json.load(a)

bot.run(data['token'])