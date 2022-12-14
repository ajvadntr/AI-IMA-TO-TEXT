##
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
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

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16, use_auth_token=True)
pipe = pipe.to("cpu")

def image_to_bytes(image):
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    return bio

def stablediffusion(bot, msg, prompt):
	
	pipe.to("cuda")
        with autocast("cuda"):
		image = pipe(prompt=[prompt])
		return image
        bot.send_photo(msg.from_user.id, photo=image_to_bytes(image))
	
