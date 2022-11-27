## --- ## ## --- ##
## --- ## ## --- ##
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from bot import Bot as app
from pyrogram import filters
from config import DBID

## --- ## ## --- ##
## --- ## ## --- ##

@app.on_message(filters.command(["start"]))
async def start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    button = [[
               InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
               InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="dallemini")
             ],[
               InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
             ]]
    id = DBID
    await client.send_message(chat_id=id, text=f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:**\n\n**Mʏ Nᴇᴡ Fʀɪᴇɴᴅ** **{message.from_user.mention}** **Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ** !")
    start = """<b>Hᴇʟʟᴏ</b> 👋 <b>{}</b>,

<b>Tʜɪs Is A Aɪ Tᴇxᴛ Tᴏ Iᴍᴀɢᴇ Bᴏᴛ</b>

<b>Yᴏᴜ Cᴀɴ Cʀᴇᴀᴛᴇ Iᴍᴀɢᴇ Fʀᴏᴍ Tᴇxᴛ Usɪɴɢ Dᴀʟʟᴇ-Mɪɴɪ</b>

<b>Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Gᴇᴛ Sᴛᴀʀᴛᴇᴅ</b>

<b>Pᴏᴡᴇʀᴇᴅ Bʏ : @AIOM_BOTS</b>"""
    await message.reply_text(
        text=start.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button),
        reply_to_message_id=message.id
    )

