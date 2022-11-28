##
import os
import base64
import replicate

os.environ['REPLICATE_API_TOKEN'] = ('98c5f3316a3844513979085dbd9621904dd71dbd')
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")

def stablediffusion(bot, msg, prompt):
	output = version.predict(prompt=prompt)
        for ele in output["images"]:
		image = base64.b64decode(ele.replace('\\n','','[',']'))
		with open(f"{msg.id}/1.jpeg","wb") as file:
			file.write(image)
        app.send_photo("{msg.id}/1.jpeg")
