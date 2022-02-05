import os

import discord
import redis
import time
from DateTime import DateTime
from discord.ext import tasks, commands
from discord.ext import commands
from dotenv import load_dotenv

t = time.time()

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)

r = redis.StrictRedis(host='192.168.200.169', port='6379', db=3, password='pollo1..')

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("ready")
    print("-------")


# class MyCog(commands.Cog):
#     def __init__(self):
#         self.printer.start()


#     def cog_unload(self):
#         self.printer.cancel()

#     @tasks.loop(seconds=5.0)
#     async def printer(self):


# a = MyCog()

@client.event
async def on_member_join(member):
    msg = f"Welcome to the my server {member.display_name}. " \
        f"You should receive a message from the Invitarr bot; follow the instructions " \
        f"to join the Plex Server"
    guild = member.guild
    role = guild.get_role(int(os.getenv("ROLE_ID")))
    await member.send(msg)
    await member.add_roles(role)

@client.event
async def on_member_update(member, member2):
    if len(member.roles) < len(member2.roles):
        for i in member2.roles:
            if i.id == 748734274156363836:
                r.set(member.id, str(DateTime(t, 'America/Chicago')))


client.run(os.getenv("TOKEN"))