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

os.environ['REPLICATE_API_TOKEN'] = ('bf8c77b4d894eba84b797264ea3021a007e81657')
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")


def stablediffusion(bot, msg, prompt):
    for image in version.predict(prompt=prompt):
        bot.send_media_group(chat_id=msg.from_user.id,
                       [
                               InputMediaPhoto(f"{image}/1.png", caption=prompt),
                               InputMediaPhoto(f"{image}/2.png", caption=prompt),
                               InputMediaPhoto(f"{image}/3.png", caption=prompt),
                               InputMediaPhoto(f"{image}/4.png", caption=prompt),
	                       InputMediaPhoto(f"{image}/5.png", caption=prompt),
	                       InputMediaPhoto(f"{image}/6.png", caption=prompt),
	                       InputMediaPhoto(f"{image}/7.png", caption=prompt),
	                       InputMediaPhoto(f"{image}/8.png", caption=prompt),
	                       InputMediaPhoto(f"{image}/9.png", caption=prompt)     
                       ]
			     )
		            
