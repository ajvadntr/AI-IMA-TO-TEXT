import os
import json
import base64
import threading
import shutil
import requests
import pyrogram
from pyrogram.types import InputMediaPhoto
from pyrogram import Client as app


reqUrl = "https://backend.craiyon.com/generate"
headersList = {"authority": "backend.craiyon.com", "accept": "application/json", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "content-type": "application/json", "dnt": "1", "origin": "https://www.craiyon.com", "pragma": "no-cache", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "Linux", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-site", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


def genrateimages(bot, msg, prompt):

	# getting the response
	payload = json.dumps({"prompt": prompt})
	response = requests.request("POST", reqUrl, data=payload, headers=headersList).json()
	os.mkdir(str(msg.id))

	# decoding base64 to image
	i = 1
	for ele in response["images"]:
		image = base64.b64decode(ele.replace('\\n',''))
		with open(f"{msg.id}/{i}.jpeg","wb") as file:
			file.write(image)
		i = i + 1 
	
	# sending images
	bot.send_media_group(msg.from_user.id,
    [
        InputMediaPhoto(f"{msg.id}/1.jpeg", caption=prompt),
        InputMediaPhoto(f"{msg.id}/2.jpeg", caption=prompt),
        InputMediaPhoto(f"{msg.id}/3.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/4.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/5.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/6.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/7.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/8.jpeg", caption=prompt),
		InputMediaPhoto(f"{msg.id}/9.jpeg", caption=prompt)
    ]
						)
