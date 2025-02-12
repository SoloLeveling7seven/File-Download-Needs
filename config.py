from pyrogram import Client, filters, idle

api_id = 28610306
api_hash = '3f57cc57f8883bd604baf3b814ffe023'
bot_token = "7580222457:AAFrfeFyi3_iHCxZbx6vvQeXt469XOqedZc" # your bot token

BIN_CHANNEL = -1002257653178 # your secret channel
BIND_ADRESS = '0.0.0.0' # your vps ip or domain

PORT = 8000 #keep it same 

FQDN = f"{BIND_ADRESS}:{PORT}"

HAS_SSL = False
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

StreamBot = Client("Downl", bot_token= bot_token , api_id= api_id, api_hash= api_hash, workers=50)
