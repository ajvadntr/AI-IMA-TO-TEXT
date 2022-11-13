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
import replicate

app = Client(
    "AI Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

os.environ['REPLICATE_API_TOKEN'] = ('98c5f3316a3844513979085dbd9621904dd71dbd')

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")

def stableimage(message, prompt):
	output = version.predict(prompt=prompt)
        await message.reply_photo(output)

reqUrl = "https://backend.craiyon.com/generate"
headersList = {"authority": "backend.craiyon.com", "accept": "application/json", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "content-type": "application/json", "dnt": "1", "origin": "https://www.craiyon.com", "pragma": "no-cache", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Linux", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#pretext = "data:image/jpeg;base64,"

# getting images and uploding
def genrateimages(message,prompt,hooo):

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
        await hooo.message.delete()
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
               InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
               InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
             ],[
               InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
             ]]
    id = int(os.environ["ID"])
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

# dalle command
@app.on_message(filters.text)
async def getpompt(client, message):
     hooo = await message.reply("**Pʀᴏᴄᴇssɪɴɢ...**")
     prompt = message.text
     id = int(os.environ["ID"])
     await app.send_message(chat_id=id, text=f"**Uꜱᴇʀ ɴᴀᴍᴇ** : **{message.from_user.mention}**\n\n**Pʀᴏᴍᴘᴛ :** {message.text}")
     ai = threading.Thread(target=lambda:genrateimages(message,prompt,hooo),daemon=True)
     si = threading.Thread(target=lambda:stableimage(message,prompt),daemon=True)
     si.start()
     ai.start()
     
#apprun
app.run()
