import discord
from dotenv import load_dotenv
import os
import requests

load_dotenv()
BARD_API_URL = os.getenv("BARD_API_URL")
BARD_SESSION_ID = os.getenv("BARD_SESSION_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


def get_bard_message(message):
    api_data = {
        "message": message,
        "session_id": BARD_SESSION_ID
    }
    
    api_request = requests.post(BARD_API_URL, json=api_data)
    return api_request.json()["content"]


class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author != self.user:
            await message.channel.send(get_bard_message(message.content))


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(DISCORD_TOKEN)
