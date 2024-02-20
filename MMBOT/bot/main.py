import secrets
import handlers

import asyncio
import logging
import sys

from aiogram import Bot, Router
from aiogram.enums import ParseMode

TOKEN = secrets.get_token()
dp = secrets.get_dispatcher()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
