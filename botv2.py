from discord.ext import commands
import discord
import time
one_code = 750087083745476659
one_vc = 750087252473806932
two_code = 750094642975998013
two_vc = 750094773913649193
import random
def process(number):
    if number == 1: return bot.get_channel(one_code), bot.get_channel(one_vc)
    else: return bot.get_channel(two_code), bot.get_channel(two_vc)
TOKEN = 'NzUxOTM1MTM1ODIxMjAxNTMw.X1QUKg.fpA12FFCpg17nW10i3foKRglU70'
SERVER = 'testing'

d = '-'

client = discord.Client()

bot = commands.Bot(command_prefix=d)

    
@bot.command(name='code', help = 'type "{}code <insert game code> <insert game number>"'.format(d))
async def code(ctx, string, number):
    print(string, number)
    if not number.isdigit() or (number.isdigit() and (int(number)>2 or int(number)<1)):
        out = 'Invalid game number'
    else:
        channel,status = process(int(number))
        new = 'GAME CODE: {}'.format(string)
        print(channel)
        await channel.edit(name = new)
        await status.edit(name = 'STATUS: IN GAME')
        out = "{} is set as the current game code for game {}".format(string, number)
    await ctx.send(out)
    
@bot.command(name='end', help = 'type "{}end <insert game number>" to end said game'.format(d))
async def end(ctx, number):
    if not number.isdigit() or (number.isdigit() and (int(number)>2 or int(number)<1)):
        out = 'Invalid game number'
    else:
        channel,status = process(int(number))
        print(number)
        await status.edit(name = 'STATUS: Not In Game')
        await channel.edit(name = 'GAME CODE: ____')
        out = "Game {} has ended".format(number)
    await ctx.send(out)

bot.run(TOKEN)
