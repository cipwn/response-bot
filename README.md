# response-bot

### A Simple Discord bot written in python3 that responds to certain words and phrases.

## Build/Run
### Requirements
- Python 3.8.0 or newer
- Pip3
- A process manager (We use PM2)
## Installing dependencies
```
sudo apt-get install python3 -y && sudo apt-get install python3-pip -y
sudo apt-get install pm2 -y
sudo apt-get update

pip3 install discord
pip3 install python-dotenv
```

### Clone the repo
```
git clone https://github.com/cipwn/response-bot
cd response-bot
```
## Modifying the bot
```
sudo nano index.py
```
- On lines 7 and 22, change "YOUR BOT TOKEN" to the token of your [discord bot](https://discord.com/developers/applications/).
## Starting the bot
```
pm2 start index.py
```
