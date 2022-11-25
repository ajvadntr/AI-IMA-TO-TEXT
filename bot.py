from aiohttp import web
from plugins import web_server

import os
import sys
import pyrogram
from datetime import datetime
import pyromod.listen
from pyrogram import Client
from pyrogram import filters
from config import PORT
from pyrogram.enums import ParseMode

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
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        self.uptime = datetime.now()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/CodeXBotz")
        self.LOGGER(__name__).info(f"aiombots")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
