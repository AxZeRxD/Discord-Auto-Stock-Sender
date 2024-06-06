import os 
import discord
import datetime
from colorama import Fore
from discord.ext import tasks, commands
from pystyle import Colors, Colorate, Write

os.system("pip install discord.py==1.7.3")
os.system("cls || clear")

TOKEN = ''


intents = discord.Intents.all()

client = commands.Bot(command_prefix='-', help_command=None, intents=intents)

content = "OK" # YOUR STOCK AD / MESSAGE

# ADD FIRST GUILD ID : [CHANNELS]
targetchnls = {
    1186362299200589824: [1245042385684271126, 1245044185455792302],
    1246751453616406549: [1246753258966356009]
}

aizer = """
                                                    ┏┓┏┳┓┏┓┏┓┓┏┓  
                                                    ┗┓ ┃ ┃┃┃ ┃┫   
                                                    ┗┛ ┻ ┗┛┗┛┛┗┛  
                                                    ┏┓┏┓┳┓┳┓┏┓┳┓  
                                                    ┗┓┣ ┃┃┃┃┣ ┣┫  
                                                    ┗┛┗┛┛┗┻┛┗┛┛┗  
                                            ══════════════════════════════════
                                        DEV : AIZER  | GITHUB : AxZeRxD  | /NUKERS
                                    ════════════════════════════════════════════════\n\n
"""

@client.event
async def on_ready():
    Write.Print(aizer, Colors.purple_to_blue, interval=0.001)
    ct = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{ct}{Fore.LIGHTBLACK_EX}] [{Fore.LIGHTGREEN_EX}INFO{Fore.LIGHTBLACK_EX}] TOKEN {Fore.LIGHTCYAN_EX}{TOKEN[:26]}******** {Fore.LIGHTBLACK_EX}ID {Fore.LIGHTCYAN_EX}{client.user.id} {Fore.LIGHTBLACK_EX}USER {Fore.LIGHTCYAN_EX}{client.user} {Fore.LIGHTBLACK_EX}STATUS {Fore.LIGHTGREEN_EX}ONLINE')
    sendmsg.start()

@tasks.loop(minutes=10)
async def sendmsg():
    ct = datetime.datetime.now().strftime('%H:%M:%S')
    for gldid, channels in targetchnls.items():
        guild = client.get_guild(gldid)
        if guild:
            for chid in channels:
                channel = discord.utils.get(guild.text_channels, id=chid)
                if channel:
                    try:
                        await channel.send(content)
                        print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{ct}{Fore.LIGHTBLACK_EX}] [{Fore.LIGHTGREEN_EX}INFO{Fore.LIGHTBLACK_EX}] GUILD {Fore.LIGHTCYAN_EX}{gldid} {Fore.LIGHTBLACK_EX}CHANNEL {Fore.LIGHTCYAN_EX}{chid} {Fore.LIGHTBLACK_EX}RESPONSE {Fore.LIGHTGREEN_EX}SENT{Fore.RESET}')
                    except Exception as e:
                        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{ct}{Fore.LIGHTBLACK_EX}] [{Fore.LIGHTRED_EX}ERROR{Fore.LIGHTBLACK_EX}] Failed to send message in Guild {gldid}, Channel {chid}: {e}{Fore.RESET}")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{ct}{Fore.LIGHTBLACK_EX}] [{Fore.LIGHTRED_EX}INFO{Fore.LIGHTBLACK_EX}] CHANNEL {chid} not found in Guild {gldid}{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{ct}{Fore.LIGHTBLACK_EX}] [{Fore.LIGHTRED_EX}INFO{Fore.LIGHTBLACK_EX}] GUILD {Fore.LIGHTCYAN_EX}{gldid} {Fore.LIGHTBLACK_EX}NOT FOUND{Fore.RESET}")

@sendmsg.before_loop
async def before_sendmsg():
    await client.wait_until_ready()

client.run(TOKEN, bot=False)
