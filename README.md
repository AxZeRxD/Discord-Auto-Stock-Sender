# Discord Bot - Auto Messenger 🤖💬


This Python script is a Discord bot that automatically sends messages to specific channels in specified guilds at regular intervals.

## Features 🚀

- Sends a predefined message to designated channels in selected guilds.
- Uses the `discord.py` library for Discord API interaction.
- Sends messages every 10 minutes using a scheduled task.
- Provides status updates in the console for successful message delivery or errors.
- Easy configuration with a simple dictionary setup for target guilds and channels.

## Requirements 📋

- Python 3.11
- `discord.py` library (`pip install discord.py==1.7.3`)
- `colorama` library (`pip install colorama`)
- `pystyle` library (`pip install pystyle`)

## Usage 💻

1. Clone this repository or download the script file.
2. Install the required libraries using pip.
3. Replace the `TOKEN` variable with your bot's token.
4. Customize the `content` variable with your desired message.
5. Modify the `targetchnls` dictionary with the desired guild and channel IDs.
6. Run the script (`python aizer.py`).

## Configuration 🛠️

- `TOKEN`: Your Discord bot's token.
- `content`: The message you want to send to the channels.
- `targetchnls`: A dictionary mapping guild IDs to lists of channel IDs where the message will be sent.

## Support ℹ️

If you encounter any issues or have any questions about using this Code, feel free to reach out for support:

- Create an issue in the GitHub repository.
- GitHub Link [AxZeRxD](https://github.com/AxZeRxD)
- Contact At Discord Server [NUKERS](https://discord.gg/nukers)
- InstaGram [mohit.4sure](https://www.instagram.com/mohit.4sure/)

## Notes 📝

- Ensure that your bot has the necessary permissions to send messages in the specified channels.
- Customize the script further as per your requirements, such as adding error handling or additional features.

## Credits 🙌

- Discord.py library: https://discordpy.readthedocs.io/en/stable/
- Colorama library: https://github.com/tartley/colorama
- Pystyle library: https://github.com/omarryhan/PyStyle

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
