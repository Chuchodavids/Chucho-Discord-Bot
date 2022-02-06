import discord
import os
import redis
import time
from datetime import date
from discord.ext import tasks, commands
from dotenv import load_dotenv
t = time.time()

load_dotenv()

guild_id = os.getenv('GUILD_ID')
tz = os.getenv('TZ')
new_invite_role_id = os.getenv('ROLE_ID')
role_gold = os.getenv('ROLE_GOLD')
redis_host = os.getenv('REDIS_IP')
redis_port = os.getenv('REDIS_PORT')
redis_db = os.getenv('REDIS_DB')
redis_pass = os.getenv('REDIS_PASS')

intents = discord.Intents.default()
intents.members = True
r = redis.StrictRedis(host=redis_host, port=int(redis_port), db=int(redis_db), password=redis_pass)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print("ready")
        print("-------")
        golden_role_members = self.get_guild(int(guild_id)).get_role(int(role_gold)).members
        MyCog(golden_role_members)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
    
    async def on_member_update(self, member, member2):
        if len(member.roles) < len(member2.roles):
            for i in member2.roles:
                if i.id == int(role_gold):
                    r.set(member.id, str(date.today()))

    async def on_member_join(self, member):
        msg = f"Welcome to the my server {member.display_name}. " \
            f"You should receive a message from the Invitarr bot; follow the instructions " \
            f"to join the Plex Server"
        guild = member.guild
        role = guild.get_role(int(new_invite_role_id))
        await member.send(msg)
        await member.add_roles(role)
    

class MyCog(commands.Cog):
    def __init__(self, member):
        self.printer.start(member)

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=5.0)
    async def printer(self, member):
        for i in member:
            if (i.id == 898436705172992011):
                print('works')


client = MyClient(intents=intents)

client.run(os.getenv("TOKEN"))
