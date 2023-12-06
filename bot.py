import os
import discord
from discord.ext import commands
from subprocess import check_output
from dotenv import load_dotenv

import command

load_dotenv()


def run_discord_bot():
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True


    bot = commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')

    @bot.command()
    async def analyze(ctx, *, args=None):
        await command.analyze(ctx)

    @bot.command()
    async def tax(ctx, *, args=None):
        await command.tax(ctx)


    @bot.command()
    async def cake(ctx, *, args=None):
        if args == "recipe":
            await command.cake(ctx)


    @bot.command()
    async def health(ctx):
        channel = ctx.channel
        await channel.send("I'm alive!")


    @bot.command()
    async def what(ctx, *, args=None):
        if args == "to do":
            await command.what_to_do(ctx)

    @bot.command()
    async def g(ctx, *, args=None):
        channel = ctx.channel

        substrings = [
            "-",
            "No meta.pkl found, assuming GPT2 encodings...",
            "number of parameters: 29.94M",
            "Overriding: start =",
            args
        ]


        if args==None:
            await channel.send("Enter seed")
              
        elif args:
            out = check_output(['python', 'nanoGPT/sample.py', '--start="%s"' % (args)], text=True)
            smallOut = out[:1999]
            res = smallOut.replace("-", "")
            test = res.replace("No meta.pkl found, assuming GPT2 encodings...", "")
            res= test.replace("number of parameters: 29.94M", "")
            test = res.replace("Overriding: start =", "")
            res = test.replace(args, "")
            test = args + res
            await channel.send(test)

      
        
    bot.run(TOKEN)



