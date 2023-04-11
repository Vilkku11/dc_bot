import os
import discord
from discord.ext import commands
from subprocess import check_output
from dotenv import load_dotenv

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
    async def gpt(ctx, *, args=None):
        channel = ctx.channel
        if args==None:
            await channel.send("Enter seed")
            
            
        elif args:
            out = check_output(['python', 'sample.py', '--start="%s"' % (args)], text=True)
            smallOut = out[:1999]
            res = smallOut.replace("-", "")
            test = res.replace("No meta.pkl found, assuming GPT2 encodings...", "")
            res = test.replace("number of parameters: 29.94M", "")
            test = res.replace("Overriding: start =", "")
            res = test.replace(args, "")
            await channel.send(res)

            
        
    bot.run(TOKEN)



