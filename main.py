import discord
import os # default module
from dotenv import load_dotenv
import datetime

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

def log(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt', 'a') as f:
            f.write('Called function with '+ ''.join([str(arg) for arg in args]) + 'at ' + str(datetime.datetime.now()) + '\n')
        val = func(*args, **kwargs)
        return val
    return wrapper


@log
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@log
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token