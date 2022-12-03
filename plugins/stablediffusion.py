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
        bot.send_photo(chat_id=msg.from_user.id, photo=f"{image}")
