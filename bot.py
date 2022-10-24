import os
import json
import base64
import threading
import shutil
import requests
import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, CallbackQuery

app = Client(
    "AI Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

# request data
reqUrl = "https://backend.craiyon.com/generate"
headersList = {"authority": "backend.craiyon.com", "accept": "application/json", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "content-type": "application/json", "dnt": "1", "origin": "https://www.craiyon.com", "pragma": "no-cache", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Linux", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#pretext = "data:image/jpeg;base64,"

# getting images and uploding
def genrateimages(message,prompt):

	# getting the response
	payload = json.dumps({"prompt": prompt})
	response = requests.request("POST", reqUrl, data=payload, headers=headersList).json()
	os.mkdir(str(message.id))

	# decoding base64 to image
	i = 1
	for ele in response["images"]:
		image = base64.b64decode(ele.replace('\\n',''))
		with open(f"{message.id}/{i}.jpeg","wb") as file:
			file.write(image)
		i = i + 1 
	
	# sending images
	app.send_media_group(message.chat.id,
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
	# archiving and uploding
	shutil.make_archive(prompt,"zip",str(message.id))
	app.send_document(message.chat.id,document=f"{prompt}.zip",caption=f'**{prompt}**\n\n**Uncompressed Images**')
	os.remove(f"{prompt}.zip")
	shutil.rmtree(str(message.id))

@app.on_message(filters.command(["start"]))
async def start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    button = [[
               InlineKeyboardButton("Tᴇxᴛ Tᴏ Iᴍᴀɢᴇ", callback_data="toim")
             ]]
    id = int(os.environ["ID"])
    await app.send_message(chat_id=id, text=f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:**\n\n**Mʏ Nᴇᴡ Fʀɪᴇɴᴅ** **{message.from_user.mention}** **Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ** !")
    await message.reply(
        text=f"""**Hᴇʟʟᴏ {message.from_user.mention}, Tʜɪs Is ᴀ Aɪ Tᴇxᴛ Tᴏ Iᴍᴀɢᴇ Bᴏᴛ**.

**Yᴏᴜ Cᴀɴ Cʀᴇᴀᴛᴇ Iᴍᴀɢᴇ Fʀᴏᴍ Tᴇxᴛ Usɪɴɢ Dᴀʟʟᴇ-Mɪɴɪ**.

**Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Gᴇᴛ Sᴛᴀʀᴛᴇᴅ**""",
        reply_markup=InlineKeyboardMarkup(button)
    )

@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "toim":
            await msg.message.edit("Sᴇɴᴅ Tᴇxᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Iᴍᴀɢᴇ")

# dalle command
@app.on_message(filters.text)
async def getpompt(client, message):
     await message.reply("**Pʀᴏᴄᴇssɪɴɢ...**")
     prompt = message.text
     id = int(os.environ["ID"])
     await app.send_message(chat_id=id, text=f"**Uꜱᴇʀ ɴᴀᴍᴇ** :**{message.from_user.mention}**\n\n**Pʀᴏᴍᴘᴛ :** ```{prompt}``` ")
     ai = threading.Thread(target=lambda:genrateimages(message,prompt),daemon=True)
     ai.start()
     
#apprun
app.run()
