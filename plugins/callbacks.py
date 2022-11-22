#©aiom|bots


from bot import app
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
