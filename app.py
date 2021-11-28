import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("ready")
    print("-------")


@client.event
async def on_member_join(member):
    msg = f"Welcome to the my server {member.display_name}. " \
          f"You should receive a message from the Invitarr bot; follow the instructions " \
          f"to join the Plex Server"
    guild = member.guild
    role = guild.get_role(int(os.getenv("ROLE_ID")))
    await member.send(msg)
    await member.add_roles(role)


client.run(os.getenv("TOKEN"))
