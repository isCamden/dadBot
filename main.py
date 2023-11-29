import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if (
        message.author != bot.user
    ):
        content = message.content.lower()
        if content.startswith("i'm "):
            name = content[4:]
            response_message = f"Hi {name}. I'm {bot.user.name}!"

        elif content.startswith("im "):
            name = content[3:]
            response_message = f"Hi {name}. I'm {bot.user.name}!"

        elif "i'm " in content:
            name = content.split("i'm ", 1)[1]
            response_message = f"Hi {name}. I'm {bot.user.name}!"

        elif " im " in content:
            name = content.split(" im ", 1)[1]
            response_message = f"Hi {name}. I'm {bot.user.name}!"

        else:
            response_message = None

        if response_message is not None:
            await message.channel.send(response_message)

    await bot.process_commands(message)

bot.run("YOUR_TOKEN_HERE") #replace with token before use
