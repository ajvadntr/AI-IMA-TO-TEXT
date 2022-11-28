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
    output = version.predict(prompt=prompt)
    with open('{msg.id}/1.jpeg', mode='wb') as file:
        img = file.read()

    output['img'] = base64.b64encode(img)
    bot.send_photo(chat_id=msg.from_user.id, image=json.dumps(data))
