#NTU5ODA3NjYyMjYzMzY5NzQ4.D3q_7Q.Lx6xYLKN1N-TJTeD2LaoTN1kEM8


import discord
from discord.ext import commands
import random
import asyncio
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='q!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def scrims(time : int):
    msg = await bot.say("The scrims will start in "+str(time)+" minutes! Prepare your self!")
    while time > 0:
      time = time - 1
      await asyncio.sleep(10)
      await bot.edit_message(msg, "The scrims will start in "+str(time)+" minutes! Prepare your self!")
      await bot.edit_message(msg, "The scrims have been started!")
    

@bot.command()
async def cookie():
    await bot.say(':cookie:')


bot.run('NTU5ODA3NjYyMjYzMzY5NzQ4.D3q_7Q.Lx6xYLKN1N-TJTeD2LaoTN1kEM8')
