## --- ## ## --- ##
## --- ## ## --- ##

from bot import Bot as app
import threading
import pyrogram
from pyrogram import filters
from plugins.dall-mini import genrateimages

## --- ## ## --- ##
## --- ## ## --- ##

@app.on_message(filters.text)
async def getpompt(client, message):
     replytext = await message.reply("**Pʀᴏᴄᴇssɪɴɢ...**")
     prompt = message.text
     id = "-1001683525472"
     await app.send_message(chat_id=id, text=f"**Uꜱᴇʀ ɴᴀᴍᴇ** : **{message.from_user.mention}**\n\n**Pʀᴏᴍᴘᴛ :** {message.text}")
     ai = threading.Thread(target=lambda:genrateimages(message,prompt),daemon=True)
     ai.start()
