import asyncio

from aiogram import Dispatcher

from app.bot.bot import bot
from app.bot.handlers import router

dp = Dispatcher()

dp.include_router(router)


def start_bot():
    asyncio.run(dp.start_polling(bot))
