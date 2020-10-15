import discord , random
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self,client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=member.guild.system_channel
        if channel is not None:
            channel.send(f"{member} has joined the {member.guild}")


    #Commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.command(aliases=["8ball"])
    async def _8ball(self,ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f"Question:{question}\nAnswer:{random.choice(responses)}")

def setup(client):
    client.add_cog(Misc(client))

