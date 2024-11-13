import discord
from discord.ext import commands, tasks
from webserver import keep_alive
import datetime
import asyncio
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print('The bot is ready')

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(name="In " + str(len(bot.guilds)) + " servers. Prefix +"))

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title='Commands',
        description='Here are the commands you can use to enhance your experience on Discord and in the Minecraft server.',
        color=discord.Color.purple()
    )
    embed.add_field(name='`+ip`', value='Displays the IP of the Minecraft server.', inline=False)
    embed.add_field(name='`+rules`', value='Classification of Minecraft server rules: major, minor, trial, and staff.', inline=False)
    embed.add_field(name='`+minor`', value='Displays minor rules.', inline=False)
    embed.add_field(name='`+major`', value='Displays major rules.', inline=False)
    embed.add_field(name='`+trial`', value='Displays rules applicable in trial.', inline=False)
    embed.add_field(name='`+staff`', value='Displays Minecraft staff rules.', inline=False)
    embed.add_field(name='`+clans`', value='Displays clan rules.', inline=False)
    embed.add_field(name='`+commands`', value='List of commands you can use on the server.', inline=False)
    embed.add_field(name='`+store`', value='Donations and ranks page.', inline=False)
    embed.add_field(name='Emergency', value='To report a bug or issue with OlympusBot, contact the creator Paulidex.', inline=False)
    embed.set_footer(text='For hiring, contact Paulidex#9510.')
    await ctx.send(embed=embed)

@bot.command()
async def a(ctx):
    await ctx.send('The bot is working correctly')

@bot.command()
async def store(ctx):
    await ctx.send('Visit our store to see our ranks and make donations ^.^ `https://olympusland.tebex.io`')

@bot.command()
async def ip(ctx):
    embed = discord.Embed(
        title='Minecraft Java Server',
        description='Version 1.16.5 - 1.17.1: play.olympusland.xyz',
        color=discord.Color.purple()
    )
    embed.set_footer(text='To see more commands, type +help')
    await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    await ctx.send('The rules are classified as major, minor, staff, and trial. To view them, type `+major` `+minor` `+staff` `+trial` `+clans`')

@bot.command(name='minor')
async def minor(ctx):
    embed = discord.Embed(
        title='Minor Rules',
        description='1) Bugs are allowed, but you must first check with staff for permission. \n'
                    '2) Do not insult other players if they do not appreciate it. \n'
                    '3) Avoid flooding (e.g., helloooooo), spamming, or unnecessary text that clutters the chat. \n'
                    '4) More than two Redstone clocks are not allowed; lag generators and chunk loaders are prohibited. \n'
                    '5) Pets are private property; it is forbidden to kill them intentionally, even if they are in an unprotected area. \n'
                    '6) Wolves cannot be used as weapons for PvP. \n'
                    '7) In isolated issues, staff may hold meetings to find a fair solution. \n'
                    '8) Do not leave a trial.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')
    await ctx.send(embed=embed)

@bot.command(name='major')
async def major(ctx):
    embed = discord.Embed(
        title='Major Rules',
        description='1) The use of multiple accounts is prohibited. If you want to change accounts, notify staff to transfer your items and properties. \n'
                    '2) Hacks are prohibited and will be sanctioned with an IP ban. \n'
                    '3) Destroying protected builds and stealing items in other players’ areas is prohibited. \n'
                    '4) Any type of killing, such as tpakill and spawn kill, is prohibited. \n'
                    '5) Exploiting bugs, such as duplication or mobility glitches, is prohibited. \n'
                    '6) The use of hacks like xray or autoclick is prohibited. \n'
                    '7) External links cannot be distributed without staff approval. \n'
                    '8) Respect staff and avoid disrespectful behavior. \n'
                    '9) Attempting to evade penalties will increase the punishment; helping another player evade is also punishable. \n'
                    '10) Lying to staff is prohibited. \n'
                    '11) Impersonating staff is prohibited. \n'
                    '12) Do not use other cases to justify actions. \n'
                    '13) Offensive messages and builds are prohibited. \n'
                    '14) Escaping jail is prohibited. \n'
                    '15) Do not help a prisoner escape jail. \n'
                    '16) Do not explore, mine, or cut trees in the normal world; use /warp resources.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')
    await ctx.send(embed=embed)

@bot.command(name='trial')
async def trial(ctx):
    embed = discord.Embed(
        title='Trial Rules',
        description='1) Do not interrupt the trial. \n'
                    '2) Present evidence. \n'
                    '3) Do not waste the judge’s time. \n'
                    '4) Read the rules before requesting a trial. \n'
                    '5) Only witnesses and involved parties are allowed in the trial. \n'
                    '6) Only Owners, Admins, and Mods can act as judges. \n'
                    '7) Both parties (accused and accusers) must be present.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')
    await ctx.send(embed=embed)

@bot.command(name='clans')
async def clans(ctx):
    embed = discord.Embed(
        title='Clan Rules',
        description='1) Any type of PvP is allowed if both players belong to a clan. \n'
                    '2) Griefing is allowed but only to clan bases.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')
    await ctx.send(embed=embed)

@bot.command(name='staff')
async def staff(ctx):
    embed = discord.Embed(
        title='Staff Rules',
        description='1) Ban complaints are handled via Discord. \n'
                    '2) Staff-exclusive items should not fall into players’ hands; both involved will be sanctioned if this happens. \n'
                    '3) Respond to players’ questions. \n'
                    '4) Greet new players. \n'
                    '5) Do not abuse power. \n'
                    '6) Only Owners, Admins, and Mods can sanction. \n'
                    '7) Treat all players equally. \n'
                    '8) Do not give players creative items; only survival items are allowed. \n'
                    '9) Be neutral in trials. \n'
                    '10) Unjustified inactivity may result in staff dismissal. \n'
                    '11) Do not reveal upcoming features to players.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')
    await ctx.send(embed=embed)

@bot.command(name='commands')
async def commands(ctx):
    embed = discord.Embed(
        title='Commands you can use on the server',
        description='/tpa (teleport to another player) \n'
                    '/tpaccept (accept teleport request) \n'
                    '/tpahere (bring another player) \n'
                    '/back (return to the previous location) \n'
                    '/sit (sit down) \n'
                    '/afk (go AFK) \n'
                    '/sethome (mark a home) \n'
                    '/home "name" (go to a marked home) \n'
                    '/delhome "name" (delete a home) \n'
                    '/ps add "name" (add a person to your protection stone) \n'
                    '/ps remove "name" (remove a person from your stone) \n'
                    '/store (see the store) \n'
                    '/stones (information about the protection stone) \n'
                    '/jobs (to earn money) \n'
                    '/jobs join "name" (join a job) \n'
                    '/jobs remove "name" (leave a job) \n'
                    '/ec (access ender chest) \n'
                    '/pay "amount" "nickname" (pay another player) \n'
                    '/money (see your money) \n'
                    '/baltop (view the richest people on Olympus) \n'
                    '/ah (auction house) \n'
                    '/ah sell "price" (sell item in hand in ah) \n'
                    '/store (buy stones, turrets, etc.) \n'
                    '/warp resources (for material gathering, building here is not recommended) \n'
                    '/warp slaughterhouse (get food) \n'
                    '/warp wedding (church) \n\n'
                    'You can create elevators by placing a quartz block with a redstone block underneath.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='To see more commands, type +help')
    await ctx.send(embed=embed)

keep_alive()
bot.run("BOT_TOKEN")
