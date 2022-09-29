# region IMPORTS

import datetime as date
from datetime import timedelta

import os
from os.path import exists
from dotenv import load_dotenv

import subprocess

import discord
from discord.ext import commands

import logging

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

import pandas as pd
# endregion


#bot = commands.Bot(command_prefix="/saki-stats ", intents=discord.Intents(messages=True, guilds=True,members=True))
intents = discord.Intents(messages=True, guilds=True, members=True)
client = discord.Client(intents=intents)

# region LOGGING
  #check for audit path
today = date.datetime.now()
logpath = "/var/log/saki-members-"+today.strftime("%Y%m%d")+".log"

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter(fmt='%(asctime)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


setup_logger('log', logpath)
log = logging.getLogger('log')


log.info(f"#######################################")
log.info(f"#### STARTING SAKI MEMBER SCRAPER  ####")
log.info(f"#######################################")

starttime=date.datetime.now()
log.info(f"Starting: {starttime}")


# endregion


# region START
today=today.strftime("%Y%m%d")
outpath = "/var/www/html/members/memberlist-"+today+".csv"
log.info(f"Output: {outpath}")

log.info(f"Starting Client")
@client.event
async def on_ready():
    for guild in client.guilds:
        log.info(f"{client.user} is scraping the following server:") 
        log.info(f"{guild.name} (id: {guild.id})")
                 
        for member in guild.members:
            line = '{},{},{},{},{},{},{},{}\n'.format(guild.name,guild.id,member.name+"#"+member.discriminator,member.display_name,member.id,member.joined_at,member.roles,member.nick)
            log.info(f"{line}")       
            
        with open(outpath, mode='w',encoding='utf8') as f:
            f.write('guild_name,guild_id,membername,display_name,memberid,joined,roles,nick\n')
            for member in guild.members:
                line = '{},{},{},{},{},{},\"{}\",{}\n'.format(guild.name,guild.id,member.name+"#"+member.discriminator,member.display_name,member.id,member.joined_at,member.roles,member.nick)
                f.write(line)
    
    endtime=date.datetime.now()
    log.info(f"End: {endtime}")
    
    await client.close()

client.run(TOKEN)

log.info(f"Exiting..... bye!")
exit()






# endregion


