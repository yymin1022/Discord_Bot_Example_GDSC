import discord
from dotenv import load_dotenv
import os

load_dotenv()
BARD_SESSION_ID = os.getenv("BARD_SESSION_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


def get_bard_message(message):
    pass


class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author != self.user:
            await message.channel.send(message.content)


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(DISCORD_TOKEN)
