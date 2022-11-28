#©aiom|bots

import os
import json
import base64
import threading
import shutil
import requests
import pyrogram
from bot import Bot as app
from config import DBID
import asyncio
from asyncio import TimeoutError
from pyrogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
from .dallmini import genrateimages
from .stablediffusion import stablediffusion

reqUrl = "https://backend.craiyon.com/generate"
headersList = {"authority": "backend.craiyon.com", "accept": "application/json", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "content-type": "application/json", "dnt": "1", "origin": "https://www.craiyon.com", "pragma": "no-cache", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Linux", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "toim":
            await msg.message.edit("Sᴇɴᴅ Tᴇxᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Iᴍᴀɢᴇ")

    if msg.data == "help":
            await msg.message.edit("help")

    if msg.data == "about":
            await msg.message.edit("about")

    if msg.data == "create":
            button = [[
               InlineKeyboardButton("• Dᴀʟʟ E Mɪɴɪ", callback_data="dallemini")
               ],[
               InlineKeyboardButton("• Sᴛᴀʙʟᴇ Dɪꜰꜰᴜsɪᴏɴ", callback_data="stablediffution")
               ],[
               InlineKeyboardButton("✘ Cʟᴏsᴇ", callback_data="close")
               ]]
            await msg.message.edit(
                text="≡ Cʜᴏᴏsᴇ Aɪ Mᴏᴅᴇʟ",
                reply_markup=InlineKeyboardMarkup(button)
            )

    if msg.data == "close":
            await msg.message.delete()

    if msg.data == "dallemini":
            await msg.message.delete()
            sssss = await bot.send_message(msg.from_user.id, text="➤ Sᴇɴᴅ Tᴇxᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Iᴍᴀɢᴇ")
            ptext = await bot.listen(msg.from_user.id, filters=filters.text, timeout=90)
            await sssss.delete(True)    
            fffff = await bot.send_message(msg.from_user.id, text="<b>Gᴇɴᴇʀᴀᴛɪɴɢ Iᴍᴀɢᴇ</b>\n<b>Esᴛ :  1 - 3 Mɪɴᴜᴛᴇs</b>")
            prompt = ptext.text
            id=DBID
            await bot.send_message(chat_id=id, text=f"<b>Uꜱᴇʀ ɴᴀᴍᴇ</b> : <b>{msg.from_user.mention}</b>\n\n<b>Pʀᴏᴍᴘᴛ :</b> {prompt}")
            dm = threading.Thread(target=lambda:genrateimages(bot,msg,prompt),daemon=True)
            dm.start()
            await asyncio.sleep(9)
            await fffff.delete(True)

    if msg.data == "stablediffution":
            await msg.message.delete()
            sssss = await bot.send_message(msg.from_user.id, text="➤ Sᴇɴᴅ Tᴇxᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Iᴍᴀɢᴇ")
            ptext = await bot.listen(msg.from_user.id, filters=filters.text, timeout=90)
            await sssss.delete(True)    
            fffff = await bot.send_message(msg.from_user.id, text="<b>Gᴇɴᴇʀᴀᴛɪɴɢ Iᴍᴀɢᴇ</b>\n<b>Esᴛ : 10s</b>")
            prompt = ptext.text
            id=DBID
            await bot.send_message(chat_id=id, text=f"<b>Uꜱᴇʀ ɴᴀᴍᴇ</b> : <b>{msg.from_user.mention}</b>\n\n<b>Pʀᴏᴍᴘᴛ :</b> {prompt}")
            dm = threading.Thread(target=lambda:stablediffusion(bot,msg,prompt),daemon=True)
            dm.start()
            await asyncio.sleep(90)
            await fffff.delete(True)
