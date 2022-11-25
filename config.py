import os

PORT = os.environ.get("PORT", "8080")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
