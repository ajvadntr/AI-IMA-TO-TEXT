#©aiom|bots


from bot import Bot as app
from config import DBID
import asyncio
from asyncio import TimeoutError
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "toim":
            await msg.message.edit("Sᴇɴᴅ Tᴇxᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Iᴍᴀɢᴇ")

    if msg.data == "help":
            await msg.message.edit("help")

    if msg.data == "about":
            await msg.message.edit("about")

    if msg.data == "close":
            await msg.message.delete()

    if msg.data == "dallemini":
            try:
                try:
                    ag = await msg.reply_text("Now send me a text")
                   _text = await bot.listen(m.chat.id, filters=filters.text, timeout=90)
                   if _text.text:
                       textp = _text.text
                       if textp == "/cancel":
                          await ag.edit("Process Cancelled Successfully")
                          return
                   else:
                       return
               except TimeoutError:
                   await ag.edit("I can't wait more for password, try again")
                   return

                botreplytext = await bot.send_message(chat_id=msg.chat.id, text="<b>Pʀᴏᴄᴇssɪɴɢ...</b>")
                prompt = textp
                id=DBID
                await bot.send_message(chat_id=id, text=f"<b>Uꜱᴇʀ ɴᴀᴍᴇ** : <b>{message.from_user.mention}</b>\n\n<b>Pʀᴏᴍᴘᴛ :</b> {message.text}")
                payload = json.dumps({"prompt": prompt})
                response = requests.request("POST", reqUrl, data=payload, headers=headersList).json()
                os.mkdir(str(msg.id))
                i = 1
                for ele in response["images"]:
	                image = base64.b64decode(ele.replace('\\n',''))
	                with open(f"{message.id}/{i}.jpeg","wb") as file:
		                file.write(image)
	                i = i + 1

                await bot.send_media_group(
                    msg.chat.id,
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
                shutil.rmtree(str(msg.id))
