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


#bot = commands.Bot(command_prefix="/saki-stats ", intents=discord.Intents(messages=True, guilds=True))
#bot.run(TOKEN)


# region LOGGING
  #check for audit path
today = date.datetime.now() - date.timedelta(days = 2)
logpath = "/var/log/saki"+today.strftime('YYmmdd')+".log"

def setup_logger(logger_name, log_file, level=logging.INFO):
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


log.info(f"################################")
log.info(f"#### STARTING SAKI SCRAPER  ####")
log.info(f"################################")

starttime=date.datetime.now()
log.info(f"Starting: {starttime}")


# endregion


# region START
path = "dotnet ~/DiscordChatExporter/DiscordChatExporter.Cli.dll"
#yesterday = date.datetime.now() - date.timedelta(days = 1)
yesterday = date.datetime.now() - date.timedelta(days = 3)

outpath = "/var/www/html/raw/%G/%C/"



#generate guilds list
guildsfile = "/var/www/html/guilds.txt"

log.info(f"#############################")
log.info(f"#### Building Guild List ####")
log.info(f"#############################")

gcmd = path + " guilds"+" -t " + TOKEN + " > " + guildsfile  
os.system(gcmd) 
gdf = pd.read_csv(guildsfile, sep="|")
gcol = gdf.iloc[:, 0]
guilds = gcol.values.tolist()

log.info(f"Guild List: {guilds}")


# endregion

log.info(f"#### Building Channel Lists")
for guild in guilds:
  log.info(f" ## Populating GuildID: {guild}")
  guild = str(guild)
  channelfile = "/var/www/html/"+guild+"-channels.txt"
  ccmd = path + " channels -g "+guild+" -t "+ TOKEN + " > " + channelfile
  os.system(ccmd)
  log.info(f"Output: {channelfile}")
  cdf = pd.read_csv(channelfile, sep="|")
  ccol = cdf.iloc[:,0]
  channels = ccol.values.tolist()
  log.info(f"Channel List: {channels}")

  #list channels:

  #export guild

  log.info(f"##########################################")
  log.info(f"#### Starting Channel Parsing: {guild}####")
  log.info(f"##########################################")
  for channel in channels:
    channel = str(channel)
    output = outpath+today.strftime("%Y%m%d")+"-"+channel+".csv"
    cmd = path + " export "+" -t " + TOKEN + " -c "+ channel + " --after "+yesterday.strftime('%Y-%m-%d')+" --before "+today.strftime('%Y-%m-%d')+" -f Csv -o "+output+" -p 10mb --dateformat 'yyyy-MM-dd HH:mm:ss.ffff'"  
  
    log.info(f"Range: {yesterday}-{today}")
    log.info(f"Channel: {channel}")
    log.info(f"Output: {output}")
    log.info(f"Complete.")
    os.system(cmd)

endtime=date.datetime.now()
log.info(f"End: {endtime}")
