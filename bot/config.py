from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    bot_token: str
    admin_chat_id: int


def get_settings() -> Settings:
    settings = Settings(
        bot_token = os.getenv('BOT_TOKEN'),
        admin_chat_id = int(os.getenv('ADMIN_CHAT_ID'))
    )
    return settings

settings = get_settings()