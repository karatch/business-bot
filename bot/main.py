import asyncio
import logging, sys

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        'Hello! This is a simple bot.\n'
        'Используйте меню ниже, чтобы посмотреть каталог или оставить заявку.'
    )


@dp.message(F.text)
async def echo(message: Message) -> None:
    await message.answer(f'echo: {message.text}')


async def main() -> None:
    bot = Bot(
        token = settings.bot_token,
        default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())