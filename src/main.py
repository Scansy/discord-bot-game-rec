import discord
import os
from dotenv import load_dotenv
from gptAPI import gpt as GPT

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
gpt = GPT()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# when someone asks to recommend a game
def recommend(msg, author):
    prompt = msg[5:]
    response = gpt.askGPT(prompt, author)
    if response:
        return response
    else:
        return "Error: empty message! Try '$rec *your question here*'"

# when someone asks to add a game
def addGame(msg, author):
    prompt = msg[5:]
    response = gpt.addGame(prompt, author)
    if response:
        return response
    else:
        return "Error: empty message! Try '$add *your game here*'"

# when bot is turned on
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# whenever bot detects a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
 
    # if msg starts with '$hello'
    if msg.startswith("$hello"):
        await message.channel.send(f"Hello {message.author}!")
    # if msg starts with '$rec'
    elif msg.startswith("$rec"):
        await message.channel.send(recommend(msg, message.author))
    # if msg starts with '$add'
    elif msg.startswith("$add"):
        await message.channel.send(addGame(msg, message.author))

client.run(DISCORD_TOKEN)