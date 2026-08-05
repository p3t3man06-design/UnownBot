from fileinput import filename

import discord
import os
import random
import flask

from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import bot
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    server = Thread(target=run_web)
    server.start()



YOUR_SERVER_ID = 1356788873329639474

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

filename = "NormalUnownGIF.gif"

TOKEN = os.getenv("DISCORD_TOKEN")

filename = "NormalUnownGIF.gif"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    change_icon.start()

@tasks.loop(minutes=1)
async def change_icon():
    global filename
    guild = bot.get_guild(YOUR_SERVER_ID)
    if random.randint(1, 5) == 1:
        if filename == "ShinyUnownGIF.gif":
            print("Already Shiny")
        else:
            filename = "ShinyUnownGIF.gif"
            with open(filename, "rb") as f:
                await guild.edit(icon=f.read())
                print("Shiny Unown detected!")
    else:
        if filename == "NormalUnownGIF.gif":
            print("Already Normal")
        else:
            filename = "NormalUnownGIF.gif"
            with open(filename, "rb") as f:
                await guild.edit(icon=f.read())
                print("Normal Unown.")

keep_alive()
# Start the bot
bot.run(TOKEN)