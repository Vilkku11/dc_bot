import discord


def test():
    print("lololol")

async def tax(ctx):
    channel = ctx.channel
    await channel.send(file=discord.File('./media/veroilmoitus_matkakulut.png'))


async def cake(ctx):
    channel = ctx.channel
    await channel.send("Cake recipe")
