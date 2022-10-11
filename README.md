# MLBB-Saki-Bot

## WHAT IS SAKI-BOT?
Saki is a Chat Log and Data Exporter for MLBB Servers, named after the delightful Magic Chess Character SAKI. 

![Saki](https://raw.githubusercontent.com/p3hndrx/MLBB-Saki-Bot/master/img/Frangipani_Saki.webp)

## HOW DOES IT WORK?
This bot consists of a series of scripts that scrape Discord Guilds (Servers) and reads available chat messages which then get translated into Comma-Spearated Values (CSV) Exports.
- This app uses the [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter/) (.NET) by Tyrrz
- It is written in Python and relies on CronJobs to execute daily exports
- Utility Scripts allow for:
  - historical scraping and backfills
  - compiling of summary tables (monthly, etc)
  - full summaries (large)
- Once scraped, the data can be parsed using your favorite Data Analysis and Visualization Apps

  ![HOW IT WORKS](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/Saki_Bot.drawio.png)
  
## WHAT ELSE IS INCLUDED?
This app comes with a Proof-of-Concept data analysis application that ingests the logs, natively, into Splunk, a professional-grade data processing engine, so that transforms can occur over the data. It does this by reading files from the hosted directories or Google Drive. Numerous count and timechart functions can be run against this data:
- ![Google Drive](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/poc-drive-channels.png?raw=true)
- ![Channel Data](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/poc-splunk-channels.png?raw=true)
- ![User Data](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/poc-user-channels.png?raw=true)
- ![Text Data](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/poc-wordcloud.png?raw=true)

## WHERE ARE WE IN THIS?
Unfortunately, we are still in a PoC phase.
We are currently have the following capabilities:
- Automated Data Scraping
- Back-fill and compiling
- RAW data hosting and transfer

Data Analysis bears a heavy processing cost, thus dashboards and reports are NOT YET AVAILABLE, but coming soon!
Some other Proof-of-Concept (more cost effective, but less-automated):
- ![PRESET.IO](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/unnamed-1.png?raw=true)
- ![Microsoft BI](https://github.com/p3hndrx/MLBB-Saki-Bot/blob/master/img/unnamed.png?raw=true)
