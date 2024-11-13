import discord  # Imports the discord.py library to interact with the Discord API.
from discord.ext import commands, tasks  # Imports additional modules to handle commands and looping tasks with discord.py.
from webserver import keep_alive  # Imports a custom function `keep_alive` to keep the bot online.
import datetime  # Imports the `datetime` library to handle and manipulate dates and times.
import asyncio  # Imports asyncio for asynchronous functions, essential for non-blocking operations.
from urllib import parse, request  # Imports modules to work with URLs and make HTTP requests.
import re  # Imports the regular expressions module `re` to analyze text patterns.

# Bot permission configuration (intents)
# Discord allows bots to use "intents" to define which events and data they can access.
# These intents control the bot’s permissions specifically, enhancing security and privacy on Discord.

# First, an intents object called `intents` is created using `discord.Intents.default()`.
# `discord.Intents.default()` returns a basic set of predefined permissions that the bot can use.
intents = discord.Intents.default()

# Next, the specific `message_content` permission is enabled in the `intents` object.
# `message_content` is a permission that allows the bot to access the text of messages in text channels.
# This permission is essential for the bot to read and respond to user commands.
# Without this permission, the bot cannot see message content and therefore cannot respond to commands.
intents.message_content = True

# Bot creation
# The bot is initialized using the `commands.Bot` class from discord.py, setting the command prefix,
# disabling the default help command, and assigning the configured intents.

# - `command_prefix="+":` Defines the prefix users must use for bot commands, in this case `+`.
#    This means that any command must start with `+`.
# - `help_command=None`: Disables the default help command from `discord.py`, allowing for a custom help command to be defined.
# - `intents=intents`: Passes the `intents` object with the configured permissions, necessary for the bot to function correctly with the established permissions.
bot = commands.Bot(command_prefix="+", help_command=None, intents=intents)


# Bot initialization event
# `@bot.event` is a decorator that indicates that the following function is a discord.py event.
# Events in discord.py are functions that automatically activate when certain events occur on Discord.

# The `on_ready` function is defined as asynchronous using `async def`, allowing the bot to perform
# multiple tasks at once without blocking other operations. This is useful in environments where the bot
# needs to respond quickly and handle multiple events simultaneously, such as messages or commands.

# `on_ready` represents the event that occurs when the bot connects to Discord and is ready to be used.
# This event activates only once, when the bot has connected and loaded all the necessary information.
@bot.event
async def on_ready():
    # The function prints the message "The bot is ready" to the console to indicate to the programmer that the bot has connected successfully.
    # This confirmation message helps verify that the connection was successful.
    print('The bot is ready')


# Looping task to change the bot's status
# `@tasks.loop` is a decorator that allows creating a looping task that executes repeatedly with a specified interval.
# In this case, an interval of 10 seconds is set, meaning the following function will execute every 10 seconds.

@tasks.loop(seconds=10)
async def change_status():
    # The `change_status` function is defined as asynchronous (using `async def`), allowing the bot to perform this
    # task in parallel with other tasks without blocking the processing of other events.

    # `await` indicates that the bot should wait until `change_presence` completes its execution before continuing.
    # This allows other tasks to execute while the bot waits, avoiding blockages in the bot’s operation.

    # `bot.change_presence` is a method that changes the bot's visible status on Discord.
    # Here, the bot shows a message in its "playing" status, indicating the number of servers it’s on and its command prefix.
    # `len(bot.guilds)` gets the number of servers the bot is present in.
    await bot.change_presence(activity=discord.Game(name="In " + str(len(bot.guilds)) + " servers. Prefix +"))


# Help command that displays an embedded message with the list of bot commands.
# `@bot.command` is a decorator that turns the following function into a command accessible to users.
# By using `@bot.command(name='help')`, a `+help` command is defined that users can type to see the list of commands.

@bot.command(name='help')
async def help(ctx):
    # The `help` function is asynchronous, allowing the bot to handle this task without blocking other operations.
    # The function receives a `ctx` parameter, representing the context in which the command was called and allowing access
    # to the channel where the response should be sent.

    # Creates an "embed" or embedded message, which is a stylized message with a title, description, fields, and other details.
    embed = discord.Embed(
        title='Commands',  # Title of the embed
        description='Here are the commands you can use to enhance your experience on Discord and in the Minecraft server.',
        color=discord.Color.purple()  # Border color of the embed, in this case, purple
    )
    # Uses `add_field` to add each command with its description in the embed.
    # The `name` parameter specifies the field name (command), and `value` specifies the description.
    # `inline=False` makes each field appear on a separate line.
    embed.add_field(name='`+ip`', value='Displays the IP of the Minecraft server.', inline=False)
    embed.add_field(name='`+rules`', value='Classification of Minecraft server rules: major, minor, trial, and staff.', inline=False)
    embed.add_field(name='`+minor`', value='Displays minor rules.', inline=False)
    embed.add_field(name='`+major`', value='Displays major rules.', inline=False)
    embed.add_field(name='`+trial`', value='Displays rules applicable in trial.', inline=False)
    embed.add_field(name='`+staff`', value='Displays Minecraft staff rules.', inline=False)
    embed.add_field(name='`+clan`', value='Displays clan rules.', inline=False)
    embed.add_field(name='`+commands`', value='List of commands you can use on the server.', inline=False)
    embed.add_field(name='`+store`', value='Donations and ranks page.', inline=False)
    embed.add_field(name='Emergency', value='To report a bug or issue with OlympusBot, contact the creator Paulidex.', inline=False)
    
    # `embed.set_footer` allows including a section at the bottom of the embedded message.
    # This footer can contain text that remains fixed and visible regardless of the fields added in the embed.
    # In this case, the footer provides contact information, indicating how to communicate for hiring purposes.
    embed.set_footer(text='For hiring, contact Paulidex#9510.')

    # `ctx.send` is a method that sends a message to the channel where the command was called.
    # `ctx` is the command context that contains information about how and where it was used, including the channel and user who executed the command.
    # `await` is used to wait until the message is sent before continuing with other operations.

    # Here, `embed=embed` indicates that the message will be sent in embed format, using the embedded message
    # that was previously defined with the title, description, commands, and footer.
    await ctx.send(embed=embed)

# Command to verify if the bot is working
# `@bot.command()` is a decorator that turns the following function into a bot command.
# Here, a command without a specific name is defined, meaning its name will be the same as the function: `a`.
# Users can type `+a` to execute this command and check if the bot is active.

@bot.command()
async def a(ctx):
    # The `a` function is asynchronous, allowing the bot to respond to this command without blocking other operations.
    # The `ctx` (context) parameter contains information about where the command was called,
    # including the channel where the response should be sent.

    # `ctx.send` is the method that sends a message to the channel from which the command was called.
    # Here, the message "The bot is working correctly" is sent as confirmation that the bot is active.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send('The bot is working correctly')  # Sends the confirmation message as a test.


# Command to send a link to the donation store
# `@bot.command()` is a decorator that turns the following function into a bot command.
# Here, a command without a specific name is defined, so the command name will be the same as the function: `store`.
# Users can type `+store` to execute this command and receive the link to the donation store.

@bot.command()
async def store(ctx):
    # The `store` function is asynchronous, allowing the bot to respond to this command without blocking other operations.
    # The `ctx` (context) parameter provides information about where the command was called,
    # including the channel where the response should be sent.

    # `ctx.send` is the method that sends a message to the channel where the command was called.
    # Here, the message includes the link to the donation store with a friendly message.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send('Visit our store to see our ranks and make donations ^.^ `https://olympusland.tebex.io`')


# Command to display the IP of the Minecraft server
# `@bot.command()` is a decorator that turns the following function into a bot command.
# Since no name is specified, the command will use the function’s name: `ip`.
# Users can type `+ip` to execute this command and receive the Minecraft server's IP address.

@bot.command()
async def ip(ctx):
    # Defines `ip` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present the information in a stylized way.
    # An embed is a visually structured message that allows including a title, description, color, and more,
    # offering an organized and attractive format for users.

    # In this embed:
    # - `title='Minecraft Java Server'` sets the embed title, which will appear at the top and in a larger text size.
    # - `description='...'` defines the main content, which includes the server IP and compatible versions.
    # - `color=discord.Color.purple()` sets a purple color for the embed’s border, making it visually prominent.
    embed = discord.Embed(
        title='Minecraft Java Server',  # Title of the embed
        description='Version 1.16.5 - 1.17.1: play.olympusland.xyz',  # Description with the server IP and versions
        color=discord.Color.purple()  # Border color of the embed
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. In this case, the footer suggests that the user
    # type `+help` to see other bot commands.
    embed.set_footer(text='To see more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, displaying the server’s IP and versions in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows how to access the server rules
# `@bot.command()` is a decorator that turns the following function into a bot command.
# Since no name is specified, the command will use the function’s name: `rules`.
# Users can type `+rules` to execute this command and receive information on how to view the server rules.

@bot.command()
async def rules(ctx):
    # The `rules` function is asynchronous, allowing the bot to respond to this command without blocking other operations.
    # The `ctx` (context) parameter provides information about where the command was called,
    # allowing the bot to send the response in the same channel.

    # `ctx.send` is the method that sends a message to the channel where the command was activated.
    # Here, the message informs that the rules are classified and suggests commands to view each type of rule.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send('The rules are classified as severe, minor, staff, and trial. To view them, type `+major` `+minor` `+staff` `+trial` `+clans`')

# Command that shows the server's minor rules
# `@bot.command(name='minor')` converts the following function into a bot command accessible to users.
# With `name='minor'`, the command is executed by typing `+minor`, allowing users to view the minor rules.

@bot.command(name='minor')
async def minor(ctx):
    # Defines `minor` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # An embed is a visually structured message that allows for including a title, description, color, and more,
    # offering an organized and attractive format for users.

    # In this embed:
    # - `title='Minor Rules'` sets the title of the embed, which will be displayed at the top in larger text.
    # - `description='...'` defines the main content, listing the server's minor rules.
    # - `color=discord.Color.purple()` sets a purple color for the embed’s border, making it visually prominent.
    embed = discord.Embed(
        title='Minor Rules',  # Title of the embed
        description='1) Bugs are allowed, but you must first check with staff for permission. \n'
                    '2) Do not insult other players if they do not appreciate it. \n'
                    '3) Avoid flooding (e.g., helloooooo), spamming, or unnecessary text that clutters the chat. \n'
                    '4) More than two Redstone clocks are not allowed; lag generators and chunk loaders are prohibited. \n'
                    '5) Pets are private property; it is forbidden to kill them intentionally, even if they are in an unprotected area. \n'
                    '6) Wolves cannot be used as weapons for PvP. \n'
                    '7) In isolated issues, staff may hold meetings to find a fair solution. \n'
                    '8) Do not leave a trial.',  # Minor rules listed in the description
        color=discord.Color.purple()  # Purple border
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands
    # and informs that the rules are cumulative.
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the rules in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows the server's severe rules
# `@bot.command(name='major')` converts the following function into a bot command accessible to users.
# With `name='major'`, the command is executed by typing `+major`, allowing users to view the severe rules.

@bot.command(name='major')
async def major(ctx):
    # Defines `major` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # The embed contains a title, a description with severe rules, and a border color.
    embed = discord.Embed(
        title='Severe Rules',  # Title of the embed
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
                    '16) Do not explore, mine, or cut trees in the normal world; use /warp resources.',  # Severe rules listed in the description
        color=discord.Color.purple()  # Purple color for the embed border
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands
    # and informs that the rules are cumulative.
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the rules in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows the trial rules
# `@bot.command(name='trial')` converts the following function into a bot command accessible to users.
# With `name='trial'`, the command is executed by typing `+trial`, allowing users to view the rules applicable in trials.

@bot.command(name='trial')
async def trial(ctx):
    # Defines `trial` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # The embed contains a title, a description with trial rules, and a border color.
    embed = discord.Embed(
        title='Trial Rules',  # Title of the embed
        description='1) Do not interrupt the trial. \n'
                    '2) Present evidence. \n'
                    '3) Do not waste the judge’s time. \n'
                    '4) Read the rules before requesting a trial. \n'
                    '5) Only witnesses and involved parties are allowed in the trial. \n'
                    '6) Only Owners, Admins, and Mods can act as judges. \n'
                    '7) Both parties (accused and accusers) must be present.',  # Trial rules listed in the description
        color=discord.Color.purple()  # Purple color for the embed border
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands
    # and informs that the rules are cumulative.
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the rules in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows clan rules
# `@bot.command(name='clans')` converts the following function into a bot command accessible to users.
# With `name='clans'`, the command is executed by typing `+clans`, allowing users to view the rules applicable to clans.

@bot.command(name='clans')
async def clans(ctx):
    # Defines `clans` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # The embed contains a title, a description with clan rules, and a border color.
    embed = discord.Embed(
        title='Clan Rules',  # Title of the embed
        description='1) Any type of PvP is allowed if both players belong to a clan. \n'
                    '2) Griefing is allowed but only to clan bases.',  # Clan rules listed in the description
        color=discord.Color.purple()  # Purple color for the embed border
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands
    # and informs that the rules are cumulative.
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the rules in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows staff rules
# `@bot.command(name='staff')` converts the following function into a bot command accessible to users.
# With `name='staff'`, the command is executed by typing `+staff`, allowing users to view the rules applicable to staff.

@bot.command(name='staff')
async def staff(ctx):
    # Defines `staff` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # The embed contains a title, a description with staff rules, and a border color.
    embed = discord.Embed(
        title='Staff Rules',  # Title of the embed
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
                    '11) Do not reveal upcoming features to players.',  # Staff rules listed in the description
        color=discord.Color.purple()  # Purple color for the embed border
    )

    # Adds a footer to the embed to provide additional context.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands
    # and informs that the rules are cumulative.
    embed.set_footer(text='Rules are cumulative, and punishments may vary depending on the person. For more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the rules in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Command that shows the available commands on the server
# `@bot.command(name='commands')` converts the following function into a bot command accessible to users.
# With `name='commands'`, the command is executed by typing `+commands`, allowing users to view a list of available server commands.

@bot.command(name='commands')
async def commands(ctx):
    # Defines `commands` as an asynchronous function to allow the bot to handle this command without interfering with other tasks.
    # The `ctx` (context) parameter provides information about where and how the command was executed,
    # allowing the bot to send the response in the same channel.

    # `embed = discord.Embed(...)` creates an embedded message or "embed" to present information in a stylized way.
    # The embed contains a title, a description with the server command list, and a border color.
    embed = discord.Embed(
        title='Commands you can use on the server',  # Title of the embed
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
                    'You can create elevators by placing a quartz block with a redstone block underneath.',  # Server commands listed in the description
        color=discord.Color.purple()  # Purple color for the embed border
    )

    # Adds a footer to the embed.
    # `set_footer` places text at the bottom of the embed. Here it suggests the user type `+help` to see more commands.
    embed.set_footer(text='To see more commands, type +help')

    # Sends the embedded message in the channel where the user executed the command.
    # `ctx.send(embed=embed)` uses the context (`ctx`) to send the embed, which presents the commands in an organized way.
    # `await` is used to wait for the message to be sent before continuing with other operations.
    await ctx.send(embed=embed)


# Calls the keep_alive function to keep the bot online on a web server.
keep_alive()

# Starts the bot. Replace "BOT_TOKEN" with the actual token of the Discord bot.
bot.run("BOT_TOKEN")

