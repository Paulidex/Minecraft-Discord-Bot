# Discord Bot for Minecraft Server Management

A Python-powered Discord bot for managing Minecraft server communities with integrated commands, rule enforcement, and a seamless connection to the Minecraft server to enhance user engagement.

## Features

- **Customizable Prefix**: Set a unique prefix to access the bot’s commands.
- **Automated Status Updates**: Updates the bot’s status every 10 seconds, displaying the number of servers it’s active in.
- **Detailed Help Command**: Users can easily access a list of available commands with `+help`.
- **Comprehensive Rule Commands**: Separate commands for different rule categories (e.g., minor, major, staff rules).
- **Minecraft Server Integration**: Provides server IP, in-game commands, and rule explanations.
- **Continuous Operation on Replit**: Keep the bot active on Replit and prevent it from disconnecting using a minimal Flask web server and UptimeRobot.

## Documentation and Code Files

The project includes four main files:

1. **Two Documented Files**: These files contain detailed comments and explanations throughout the code to help users understand the bot's functionality and structure.
2. **Two Undocumented Files**: These files provide a streamlined version of the bot’s code without inline comments. They’re ideal for deployment or for users who prefer a cleaner codebase.

Having both documented and undocumented versions allows users to choose the file that best suits their needs—whether they want to understand the code in detail or work with a minimal, efficient setup.

## Requirements

- **Python 3.6+**
- `discord.py` library for Discord API interaction
- `Flask` for web server functionality

Install dependencies with:
```bash
pip install discord flask
```

## Usage

### 1. Clone or Download the Project
   
   ```bash
   git clone https://github.com/yourusername/minecraft-discord-bot.git
   cd minecraft-discord-bot
   ```

### 2. Set Up Your Bot Token

   Replace `"YOUR_BOT_TOKEN"` in the `bot.run()` function with your actual Discord bot token.

### 3. Upload the Project to Replit

   - Upload the code to Replit and run the bot in the cloud to keep it active continuously.
   - Configure the bot to use a minimal “Keep Alive” web server on Replit so UptimeRobot can monitor it and keep the bot running.

### 4. Set Up Uptime with UptimeRobot

   To keep the bot active 24/7, follow these steps on [UptimeRobot](https://uptimerobot.com):

   - Create an account on UptimeRobot and select “Add New Monitor.”
   - Choose the HTTP monitor type.
   - Enter your project URL from Replit (something like `https://your-repl-name.your-username.repl.co`).
   - Set the check frequency (for example, every 5 minutes).
   - This will allow UptimeRobot to continuously check your Replit project, preventing it from disconnecting.

### 5. Run the Bot on Replit
   
   Start the bot on Replit by running `python bot.py`. As long as UptimeRobot monitors your Replit page, the bot will stay active.

## Commands

### General Commands

- **`+help`**: Lists all commands and descriptions.
- **`+ip`**: Displays the Minecraft server’s IP address.
- **`+store`**: Shares a link to the server’s online donation store.
- **`+rules`**: Introduces server rules, categorized by severity.

### Rule Commands

Each command below provides users with specific server rules:

- **`+minor`**: Minor rule violations
- **`+major`**: Major rule violations
- **`+trial`**: Trial rules
- **`+staff`**: Staff-specific rules
- **`+clans`**: Clan rules

### Minecraft Commands

- **`+commands`**: Lists all available in-game commands, such as teleportation and economic commands.

## Continuous Operation with UptimeRobot and Replit

To prevent the bot from disconnecting, especially on Replit, the project is set up with a web page on Replit and kept active by UptimeRobot, which continually checks its availability.

## Tutorial

For a detailed visual setup guide, follow the next tutorial that is on YouTube:  
[![YouTube Tutorial](https://img.youtube.com/vi/SPTfmiYiuok/0.jpg)](https://youtu.be/SPTfmiYiuok)

This video shows how to upload the bot to Replit and configure it with UptimeRobot to keep it active 24/7.
