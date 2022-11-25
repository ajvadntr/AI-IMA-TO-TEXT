import os
import logging

PORT = os.environ.get("PORT", "8080")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
