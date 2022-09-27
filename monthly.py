import pandas as pd
import glob
import os
import re
import datetime
today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)

import logging

# region LOGGING
  #check for audit path
logpath = "/var/log/saki-monthly-"+today.strftime("%Y%m%d")+".log"


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


log.info(f"##############################################")
log.info(f"#### STARTING MONTHLY SUMMARIZER SCRAPER  ####")
log.info(f"##############################################")



# endregion


log.info(f"Running: {today}")
lm = last_month.strftime("%Y%m")

rawpath = "/var/www/html/raw"

log.info(f"Checking: {rawpath}")

guilds = os.listdir(rawpath)
log.info(guilds)

files_path = [os.path.join(rawpath,x) for x in guilds]
log.info(files_path)

for guild in files_path:
    channels = os.listdir(guild)
    log.info(f"Guild:: {guild}")
    log.info(f"Channels:\n{channels}")
    channels_path = [os.path.join(rawpath,guild,channel) for channel in channels]
    
    log.info(f"Paths:\n")
    log.info(channels_path)

    for c in channels_path:
        logs = os.listdir(c)
        #log.info(logs)
        log.info(f"Selecting:\n {c}/{lm}*")
        lm_log = [k for k in logs if lm in k]
        
        count = len(lm_log)
        
        if count == 0:
          log.info(f"Channel is empty for {lm}... Skipping...")

        else:
          logs_path = [os.path.join(guild,c,k) for k in lm_log]
          log.info(logs_path)

          log.info(f"Found: {count} logs")
          files = os.path.join(rawpath,guild,c, f'{lm}*.csv')
          files = glob.glob(files)
          df = pd.concat(map(pd.read_csv, files), ignore_index=True)
          log.info(df)

          chan = lm_log[0]
          chan = chan.replace(".csv","")
          chan = re.sub("[0-9]{8}-",'',chan)
          
          outpath = c.replace("raw","monthly")
          if not os.path.exists(outpath):
            os.makedirs(outpath)

          output = os.path.join(outpath,f"{lm}-{chan}.csv")
          log.info(f"Saving to:\n{output}")
          df.to_csv(output,index=False)
