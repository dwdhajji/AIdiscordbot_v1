import openai
import discord
from discord.ext import commands

openai.api_key = "YOUR OPENAI KEY"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("BOT IS ONLINE. dwd_010#0001")

@bot.command()
async def chat(ctx, message: str="Hello, how can I help you?"):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message
    )
    try:
        await ctx.send(response["choices"][0]["text"] + " ")
    except IndexError:
        await ctx.send("Sorry, I couldn't generate a response to your message!")

@bot.command()
async def chat_openai(ctx):
    message = await ctx.send("Hello, how can I help you?")
    while True:
        response = await bot.wait_for('message')
        if response.content == 'stop':
            await ctx.send('Bye!')
            break
        else:
            openai_response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=response.content
            )
            try:
                await ctx.send(openai_response["choices"][0]["text"] + "")
            except IndexError:
                await ctx.send("Sorry, I couldn't generate a response to your message!")

@bot.command()
async def greet(ctx):
    await ctx.send("Hello! It's nice to meet you! 😊")

@bot.command()
async def hello(ctx):
    await ctx.send("Hi there! What can I do for you? 🤔")

bot.run("YOUR BOT TOKEN")