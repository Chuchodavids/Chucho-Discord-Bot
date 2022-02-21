import discord
import os
from dotenv import load_dotenv
import helpers.db_helper as db_helper

db = db_helper.sqldb()
db.check_table()
# ----- env variables ------
load_dotenv()
tz = os.getenv('TZ')
new_invite_role_id = os.getenv('ROLE_ID')
role_gold = os.getenv('ROLE_GOLD')
guild_id = os.getenv('GUILD_ID')

# ---- Discord -----
intents = discord.Intents.default()
intents.members = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print("ready")
        print("-------")

    async def on_member_update(self, member, member2):
        if len(member.roles) < len(member2.roles):
            for role in member2.roles:
                if role.id == int(role_gold):
                    db.insert(member.id, member.name)

    async def on_member_join(self, member):
        msg = f"Welcome to the my server {member.display_name}. " \
            f"You should receive a message from the Invitarr bot; follow the instructions " \
            f"to join the Plex Server"
        guild = member.guild
        role = guild.get_role(int(new_invite_role_id))
        await member.send(msg)
        await member.add_roles(role)

client = MyClient(intents=intents)

client.run(os.getenv("TOKEN"))
