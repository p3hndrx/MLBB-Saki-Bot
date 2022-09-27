# region IMPORTS

import datetime as date
from datetime import timedelta

import os
from os.path import exists

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
logpath = "/var/log/saki-monthly-backfill-"+today.strftime('%Y%m%d')+".log"

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


log.info(f"##########################################")
log.info(f"#### STARTING BACKLOG PARSER SCRAPER  ####")
log.info(f"##########################################")

starttime=date.datetime.now()
log.info(f"Starting: {starttime}")


# endregion


# region START





# endregion
