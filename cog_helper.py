from discord.ext import tasks, commands
import db_helper

class MyCog(commands.Cog):
    def __init__(self, members):
        self.task.start(members)

    def cog_unload(self):
        self.task.cancel()

    @tasks.loop(minutes=5.0)
    async def task(self, members):
        for i in members:
            if (i.id == 898436705172992011):
                print('works')