import ssl
import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path

from pyrogram import Client, filters, idle
from server import web_server
from pyrogram import idle
from aiohttp import web

from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.human_readable import humanbytes
from asyncio import TimeoutError
from utils.file_properties import get_name, get_hash, get_media_file_size
from config import StreamBot,URL, FQDN, BIN_CHANNEL, BIND_ADRESS, PORT


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)


@StreamBot.on_message(filters.text & filters.command('start'))
async def okzz(c: Client, m: Message):
    await m.reply("Send me any file to get direct download link")
                      

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo))
async def private_receive_handler(c: Client, m: Message):
    try:

        log_msg = await m.forward(chat_id=BIN_CHANNEL)
        
        online_link = f"{URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        
        photo_xr="https://telegra.ph/file/3cd15a67ad7234c2945e7.jpg"
        
        

        msg_text ="""
<b>ʏᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡

<b>📧 ғɪʟᴇ ɴᴀᴍᴇ :- </b> <i><b>{}</b></i>

<b>📦 ғɪʟᴇ sɪᴢᴇ :- </b> <i><b>{}</b></i>

<b>💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- </b> <i><b>{}</b></i>
"""

        await m.reply_text(
            
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link),
            
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚡ ᴅᴏᴡɴʟᴏᴀᴅ ⚡', url=online_link)]]) #Download Link
        )
    except Exception as e:
        print(e)



async def start_services():
  print('------------------- Initalizing Telegram Bot -------------------')
  ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  ssl_context.load_cert_chain('domain.crt', 'domain.key')
  app = web.AppRunner(await web_server())
  await app.setup()
  await web.TCPSite(app, BIND_ADRESS, PORT,ssl_context=ssl_context).start()
  print('------------------- Finished Telegram Bot -------------------')
  
  


if __name__ == '__main__':
  StreamBot.start()
  StreamBot.loop.create_task(start_services())
  idle()
  
