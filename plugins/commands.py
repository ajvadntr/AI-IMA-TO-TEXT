## --- ## ## --- ##
## --- ## ## --- ##
import os
import json
import base64
import threading
import shutil
import requests
import pyrogram
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from bot import Bot as app
import threading
from pyrogram import filters
from config import DBID

## --- ## ## --- ##
## --- ## ## --- ##

reqUrl = "https://backend.craiyon.com/generate"
headersList = {"authority": "backend.craiyon.com", "accept": "application/json", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "content-type": "application/json", "dnt": "1", "origin": "https://www.craiyon.com", "pragma": "no-cache", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Linux", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


@app.on_message(filters.command(["hhh"]))
async def getpompt(client, message):
     botreplytext = await client.send_message(chat_id=message.chat.id, text="<b>Pʀᴏᴄᴇssɪɴɢ...</b>")
     prompt = message.text
     id=DBID
     await client.send_message(chat_id=id, text=f"**Uꜱᴇʀ ɴᴀᴍᴇ** : **{message.from_user.mention}**\n\n**Pʀᴏᴍᴘᴛ :** {message.text}")

     payload = json.dumps({"prompt": prompt})
     response = requests.request("POST", reqUrl, data=payload, headers=headersList).json()
     os.mkdir(str(message.id))

     i = 1
     for ele in response["images"]:
	     image = base64.b64decode(ele.replace('\\n',''))
	     with open(f"{message.id}/{i}.jpeg","wb") as file:
		     file.write(image)
	     i = i + 1

     await client.send_media_group(
         message.chat.id,
         [
                InputMediaPhoto(f"{message.id}/1.jpeg", caption=prompt),
                InputMediaPhoto(f"{message.id}/2.jpeg", caption=prompt),
                InputMediaPhoto(f"{message.id}/3.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/4.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/5.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/6.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/7.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/8.jpeg", caption=prompt),
		InputMediaPhoto(f"{message.id}/9.jpeg", caption=prompt)
         ]
    )
     shutil.rmtree(str(message.id))

@app.on_message(filters.command(["start"]))
async def start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    button = [[
               InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
               InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
             ],[
               InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
             ]]
    id = DBID
    await app.send_message(chat_id=id, text=f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:**\n\n**Mʏ Nᴇᴡ Fʀɪᴇɴᴅ** **{message.from_user.mention}** **Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ** !")
    start = """**Hᴇʟʟᴏ** 👋 **{}**,
**Tʜɪs Is A Aɪ Tᴇxᴛ Tᴏ Iᴍᴀɢᴇ Bᴏᴛ**
**Yᴏᴜ Cᴀɴ Cʀᴇᴀᴛᴇ Iᴍᴀɢᴇ Fʀᴏᴍ Tᴇxᴛ Usɪɴɢ Dᴀʟʟᴇ-Mɪɴɪ**
**Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Gᴇᴛ Sᴛᴀʀᴛᴇᴅ**
**Pᴏᴡᴇʀᴇᴅ Bʏ : @AIOM_BOTS**"""
    await message.reply_text(
        text=start.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button)
    )

