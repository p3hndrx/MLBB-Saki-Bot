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

#bot = commands.Bot(command_prefix="/saki-stats ", intents=discord.Intents(messages=True, guilds=True))
#bot.run(TOKEN)


# region LOGGING
  #check for audit path
logpath = "/var/www/html/saki.log"

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
  #add CSV header if doesn't exist
# endregion



path = "dotnet ~/DiscordChatExporter/DiscordChatExporter.Cli.dll"
#yesterday = date.datetime.now() - date.timedelta(days = 1)
yesterday = date.datetime.now() - date.timedelta(days = 375)
today = date.datetime.now()

outpath = "/var/www/html/log/%G/%C/"

channels = ["947676939357913148","895169608653353031", "853816389499748382", "853816389499748382"]

starttime=date.datetime.now()
log.info(f"Starting: {starttime}")

for channel in channels:
  output = outpath+today.strftime("%Y%m%d")+"-"+channel+".csv"
  cmd = path + " export "+" -t " + TOKEN + " -c "+ channel + " --after "+yesterday.strftime('%Y-%m-%d')+" --before "+today.strftime('%Y-%m-%d')+" -f Csv -o "+output+" -p 10mb --dateformat 'yyyy-MM-dd'"  

  log.info(f"Range: {yesterday}-{today}")
  log.info(f"Channel: {channel}")
  log.info(f"Command: {cmd}")
  os.system(cmd)
  print(cmd)
  #f = open(logpath,"w")
  #result = subprocess.check_output(cmd,shell=True,stdout=f)
  #result = subprocess.call(cmd,shell=True,stdout=f)
  log.info(f"{result}")

endtime=date.datetime.now()
log.info(f"End: {endtime}")
