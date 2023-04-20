import discord
import random


def test():
    print("lololol")

async def tax(ctx):
    channel = ctx.channel
    await channel.send(file=discord.File('./media/veroilmoitus_matkakulut.png'))
    await channel.send(file=discord.File('./media/perusverokortti-palkka.pdf'))


async def health(ctx):
    channel = ctx.channel


async def what_to_do(ctx):
    channel = ctx.channel
    random.seed()
    num = random.randint(0,2)
    print(num)
    if num == 0:
        await channel.send("""You seem to be hungry.
        You should eat something!""")
    elif num == 1:
        await channel.send("""Get some sleep""")
    elif num == 2:
        await channel.send("""Get up and get moving!""")

async def cake(ctx):
    channel = ctx.channel
    await channel.send(""" ```Citrus, almond & yogurt cake
    
    Ingredients

    165g butter, plus extra for the tin
    200g golden caster sugar, plus 2 tbsp
    150g self-raising flour
    100g ground almonds
    3 eggs
    75g natural yogurt, plus 2 tbsp
    1 large lemon
    1 orange
    100g icing sugar
    15g toasted flaked almonds```
    
    """)
    await channel.send("""
    How to make:

```
STEP 1

Melt the butter in a small pan. Remove from the heat and leave to cool slightly. Meanwhile, butter a 23cm springform cake tin and line with baking parchment. Heat the oven to 180C/160C fan/gas 4.

STEP 2

Put the 200g caster sugar, flour and ground almonds in a large bowl and mix well. Whisk the eggs and 75g yogurt into the cooled melted butter, then pour this into the bowl with the dry ingredients. Zest the lemon and orange over the bowl. Stir with a spatula until there are no streaks of flour, then scrape into the tin and bake on the middle shelf of the oven for 40 mins.

STEP 3

Cut a few slices each from the zested lemon and orange, then squeeze the juice from what’s left of each into a saucepan (you’ll need about 6 tbsp total). Add the 2 tbsp caster sugar and the fruit slices to the pan. Bring to the boil and cook for 5-10 mins, or until the juice has reduced to a thin syrup and the fruit slices have softened. Leave to cool. Remove the fruit slices to a sheet of baking parchment and leave to dry.

STEP 4

Insert a skewer into the middle of the cake – it should come out dry, with no wet cake mix clinging to it. If it’s not ready, bake for 5-10 mins more and check again. Leave to cool in the tin for 5 mins, then spoon over the citrus syrup. Leave to cool for 10 mins more, then remove from the tin. To freeze, first leave to cool completely, then wrap the cake well. Will keep frozen for up to three months.

STEP 5

Mix the 2 tbsp yogurt with the icing sugar to make a thick icing. Spoon this onto the centre of the cake and use the back of a spoon to ease it to the edge (it should drip over the side). Scatter over the flaked almonds and decorate with the fruit slices. Serve warm, or leave to cool completely. Will keep in an airtight tin for up to five days.```""")
