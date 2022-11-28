##
import io
from io import BytesIO
import os
from PIL import Image
import base64
import replicate
import json
import base64
from pyrogram.types import InputMediaPhoto

os.environ['REPLICATE_API_TOKEN'] = ('98c5f3316a3844513979085dbd9621904dd71dbd')
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")



def stablediffusion(bot, msg, prompt):
    output = version.predict(prompt=prompt, num_outputs=9)
    i = 1
    for ele in output["images"]:
	    image = base64.b64decode(ele.replace('\\n',''))
	    with open(f"{msg.id}/{i}.jpeg","wb") as file:
	            file.write(image)
	    i = i + 1
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
