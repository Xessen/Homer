import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot is ready.")



@client.command()
async def load(ctx,extention):
    client.load_extension(f"cogs.{extention}")

@client.command()
async def unload(ctx,extention):
    client.unload_extension(f"cogs.{extention}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("NzU4MzAwMTkzNzMyMDM0NTcx.X2s8Fg.dCm0BjSCsR_sr0DJsX_8yvJUQ44")