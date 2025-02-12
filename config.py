from pyrogram import Client, filters, idle

api_id = xx
api_hash = 'xx'
bot_token = "xx" # your bot token

BIN_CHANNEL = -1002257653178 # your secret channel
BIND_ADRESS = '159.89.168.247' # your vps ip 

PORT = 8000 #keep it same 

FQDN = f"{BIND_ADRESS}:{PORT}"

HAS_SSL = False
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

StreamBot = Client("Downl", bot_token= bot_token , api_id= api_id, api_hash= api_hash, workers=50)
