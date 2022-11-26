## --- ## ## --- ##
## --- ## ## --- ##

from bot import Bot as app
import threading
import pyrogram
from pyrogram import filters
from .dallmini import genrateimages
from config import DBID

## --- ## ## --- ##
## --- ## ## --- ##

@app.on_message(filters.text)
async def getpompt(client, message):
     botreplytext = await client.send_message(chat_id=message.chat.id, text="<b>Pʀᴏᴄᴇssɪɴɢ...</b>")
     prompt = message.text
     id=DBID
     await client.send_message(chat_id=id, text=f"**Uꜱᴇʀ ɴᴀᴍᴇ** : **{message.from_user.mention}**\n\n**Pʀᴏᴍᴘᴛ :** {message.text}")
     ai = threading.Thread(target=lambda:genrateimages(message,prompt),daemon=True)
     ai.start()
