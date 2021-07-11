import typing

import voxelbotutils as vbu


class ChemistryCommands(vbu.Cog):

    def __init__(self, bot):
        super().__init__(bot)
        self.responses = {
            "aeration": "Aeration is the process of incorporating air into food products to increase the volume and create a light, airy texture.\nFood can be aerated by:\n-*Biological ingredients:* yeast\n-*Chemical ingredients:* baking powder, bicarbonate of soda.\n-*Mechanical actions:* like sifting, creaming, whisking, beating, folding ingredients and rubbing in ingredients",
            "caramelisation": "Caramelisation is when sugar (sucrose) begins to decompose when exposed to high temperatures (190°C or 374°F) using dry heat. An example would be caramel!",
            "coagulation": "Coagulation is a form of denaturation (see `!b denaturation` for more info) that occurs when there is a permanent change in the protein from a liquid into a thick mass as a result of heat or the addition of acids. A food example would be cooking eggs",
            "denaturation": "Denaturation describes the permanent structural change of the protein molecules in food like beef. This can occur by the application of heat, mechanical action or the addition of acids.",
            "dextrinization": "Dextrinization is the process that occurs when a starch is exposed to dry heat; the starch is broken down into dextrin which results in a golden brown colour. Found in foods like toast!",
            "emulsification": "Emulsification is mixing two immiscible liquids (liquids that don’t normally combine), for example water and oil. Some proteins, like lecithin found in egg yolk, act as emulsifying agents and hold the immiscible liquids in suspension. It is found in foods like mayonnaise.",
            "gelatinization": "Gelatinization is the process in which starch granules absorb liquid in the presence of heat which causes starch granules to burst and release molecules thus thickening the liquid, forming a gel.",
            "maillard": "Maillard turns food brown and creates pleasant, volatile, aromatic compounds as seen in foods like cookies It is a reaction between amino acids in protein and sugars or starch and it beings at 154°C (309°F).",
        }

    @vbu.command(name='chemistry', aliases=['chem'])
    async def _chemistry_command(self, ctx:vbu.Context, reaction:typing.Optional[str]=None):
        """
        Get some info on chemical reactions that occur within cooking
        """
        
        if reaction is not None:
            try:
                await ctx.send(self.responses[reaction])
            except KeyError:
                await ctx.send('That reaction doesn\'t exist')
            return

        with vbu.Embed(use_random_colours=True) as embed:
            embed.set_author(name='Chemical reactions that occur within cooking')
            embed.description = f'Use as `{ctx.clean_prefix}chem [reaction name]`\n\n'+', '.join(f'`{k}`' for k in self.responses.keys())
            await ctx.send(embed=embed)


def setup(bot:vbu.Bot):
    x = ChemistryCommands(bot)
    bot.add_cog(x)
