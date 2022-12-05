import pyrogram
from pyrogram import Client


Bot = Client(
    "Pyrogram Bot",
    bot_token = "5676297902:AAGYG022_mQe0VhLdzdEGsQZATGVc9NCa6Q",
    api_id = "6146411",
    api_hash = "279c5805accac5a35f6bc8c2e38ac036",
    plugins=dict(root="plugins")
)

Bot.run()
