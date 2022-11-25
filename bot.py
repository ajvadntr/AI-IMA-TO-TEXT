import os
import io
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
from config import PORT

class app(Client):
    def __init__(self):
        super().__init__(
            name= "Text2Image",
            api_hash= "279c5805accac5a35f6bc8c2e38ac036",
            api_id= "6146411",
            plugins={
                "root": "plugins"
            },
            workers= "4",
            bot_token= "5676297902:AAGYG022_mQe0VhLdzdEGsQZATGVc9NCa6Q"
        )

    
#apprun
app.run()
