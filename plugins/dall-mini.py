import os
import json
import base64
import threading
import shutil
import requests
import pyrogram
from pyrogram.types import InputMediaPhoto




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
