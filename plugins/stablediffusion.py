##
import io
import os
import base64
import replicate

os.environ['REPLICATE_API_TOKEN'] = ('98c5f3316a3844513979085dbd9621904dd71dbd')
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")


def image_to_bytes(output):
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    return bio

def stablediffusion(bot, msg, prompt):
	output = version.predict(prompt=prompt)
        app.send_photo(image_to_bytes(output))
