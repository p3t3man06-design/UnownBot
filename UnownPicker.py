from fileinput import filename

import discord
import os
import random
import flask
import socket
import time
import requests
from datetime import datetime


from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import bot
from flask import Flask, jsonify
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

# Configuration
HEALTHZ_URL = "https://unownbot.onrender.com"  # Change to your service URL
INTERVAL_SECONDS = 5 * 60  # 5 minutes

def ping_healthz():
    """Ping the /healthz endpoint and log the result."""
    try:
        response = requests.get(HEALTHZ_URL, timeout=5)  # 5s timeout
        status_code = response.status_code
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if status_code == 200:
            print(f"[{timestamp}] ✅ Healthy ({status_code}) - {response.text}")
        else:
            print(f"[{timestamp}] ⚠️ Unhealthy ({status_code}) - {response.text}")

    except requests.exceptions.RequestException as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ❌ Error: {e}")


YOUR_SERVER_ID = 1356788873329639474

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

filename = "NormalUnownGIF.gif"

TOKEN = os.getenv("DISCORD_TOKEN")

filename = "NormalUnownGIF.gif"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    if not change_icon.is_running():
        change_icon.start()

    if not health_check.is_running():
        health_check.start()

@tasks.loop(minutes=5)
async def health_check():
    try:
        response = requests.get(HEALTHZ_URL, timeout=5)
        print(f"{response.status_code}: {response.text}")
    except Exception as e:
        print(e)

@tasks.loop(hours=24)
async def change_icon():
    global filename
    guild = bot.get_guild(YOUR_SERVER_ID)
    if random.randint(1, 20) == 1:
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
